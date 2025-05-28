import requests
from constants import (
    CClerkCrawlerConstants,
    PDF_DIRECTORY,
    RAW_RESPONSES,
)
from log_handler import _logger
from lxml import etree
import os
import urllib
from models import ValidateData
from airtable_manager import AirtableManager
from uuid import uuid4


class CClerkCrawler:
    def __init__(self):
        self.airtable_manager = AirtableManager()
        self.event_validation = None
        self.view_state = None

    def home_page_request(self):
        _logger.info("Starting home page request for CClerkCrawler...")
        response = requests.post(
            "https://www.cclerk.hctx.net/Applications/WebSearch/FRCL_R.aspx",
            headers=CClerkCrawlerConstants.headers.value,
            data=CClerkCrawlerConstants.data.value,
        )
        if response.status_code == 200:
            _logger.info("Home page request successful.")

            with open(os.path.join(RAW_RESPONSES, "page_1.html"), "wb") as file:
                file.write(response.text.encode("utf-8"))
            return response
        else:
            _logger.error(
                f"Failed to retrieve home page. Status code: {response.status_code}"
            )
            return False

    def extract_doclinks(self, response):
        """
        Extracts all hrefs from doclinks in the response HTML.
        Returns a list of valid href strings.
        """
        try:
            if not response or not hasattr(response, "text"):
                _logger.error("Invalid response object passed to extract_doclinks.")
                return []

            tree = etree.HTML(response.text)
            hrefs = tree.xpath(
                "//table[contains(@class,'table table-hover table-striped table-responsive table-condensed')]//a[contains(@class,'doclinks')]/@href"
            )
            document_names = tree.xpath(
                "//table[contains(@class,'table table-hover table-striped table-responsive table-condensed')]//a[contains(@class,'doclinks')]/text()"
            )
            # Filter out empty or malformed hrefs
            valid_hrefs = [
                href for href in hrefs if isinstance(href, str) and href.strip()
            ]
            _logger.info(f"Found {len(valid_hrefs)} valid doclink hrefs .")
            if not valid_hrefs:
                _logger.warning("No valid doclink hrefs found in the response.")
                return [],[]
            else:
                _logger.info(f"Extracted {len(valid_hrefs)} doclink hrefs.")
                return valid_hrefs, document_names
        except Exception as e:
            _logger.error(f"Error extracting doclinks: {e}")
            return False,False

    def download_pdf(self, pdf_href):
        """
        Downloads a PDF from the given href and returns the response if successful.
        """
        pdf_doc_complete_url = (
            f"https://www.cclerk.hctx.net/Applications/WebSearch/{pdf_href}"
        )
        try:
            _logger.info(f"Attempting to download PDF from: {pdf_doc_complete_url}")
            response = requests.get(
                pdf_doc_complete_url,
                headers=CClerkCrawlerConstants.headers.value,
                stream=True,
            )
            if response.status_code == 200:
                _logger.info(f"Successfully downloaded PDF: {pdf_href}")
                return response
            else:
                _logger.error(
                    f"Failed to download PDF: {pdf_href}. Status code: {response.status_code}, Content-Type: {response.headers.get('Content-Type')}"
                )
                return None
        except Exception as e:
            _logger.error(f"Exception occurred while downloading PDF {pdf_href}: {e}")
            return None

    def save_pdf(self, response, filename):
        """
        Saves the PDF response content to the PDF_DATA folder with the given filename.
        Returns True if successful, False otherwise.
        """
        try:
            if not response or response.status_code != 200:
                _logger.error("Invalid response object or status code for saving PDF.")
                return False
            content_type = response.headers.get("Content-Type", "").lower()
            if not content_type.startswith("application/pdf"):
                _logger.error(
                    f"Response content is not a PDF. Content-Type: {content_type}"
                )
                return False

            pdf_path = os.path.join(PDF_DIRECTORY, filename)
            with open(pdf_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            _logger.info(f"PDF saved successfully at {pdf_path}")
            return True
        except Exception as e:
            _logger.error(f"Exception occurred while saving PDF {filename}: {e}")
            return False

    def get_view_state_and_event_validation(self, home_page_response):
        try:
            if not home_page_response or not hasattr(home_page_response, "text"):
                _logger.error(
                    "Invalid response object passed to get_view_state_and_event_validation."
                )
                return False

            tree = etree.HTML(home_page_response.text)
            view_state = tree.xpath("//input[@id='__VIEWSTATE']/@value")[0]
            event_validation = tree.xpath("//input[@id='__EVENTVALIDATION']/@value")[0]
            self.view_state = view_state
            self.event_validation = event_validation
        except Exception as e:
            _logger.error(f"Error getting view state and event validation: {e}")
            return False

    def get_next_page_data(self, page_count, month):
        _logger.info(f"Fetching data for page {page_count} of month {month}...")
        view_state = urllib.parse.quote(self.view_state)
        event_validation = urllib.parse.quote(self.event_validation)
        page_number = f"Page${page_count}"
        page_number_encoded = urllib.parse.quote(page_number)
        data = f"ctl00%24ScriptManager1=ctl00%24ContentPlaceHolder1%24UpdatePanelAddtoCart%7Cctl00%24ContentPlaceHolder1%24GridView1&ctl00%24ContentPlaceHolder1%24hfSearchType=0&ctl00%24ContentPlaceHolder1%24hfViewCopyOrders=False&ctl00%24ContentPlaceHolder1%24hfViewECart=False&ctl00%24ContentPlaceHolder1%24txtFileNo=&ctl00%24ContentPlaceHolder1%24rbtlDate=SaleDate&ctl00%24ContentPlaceHolder1%24ddlYear=2024&ctl00%24ContentPlaceHolder1%24ddlMonth={month}&__LASTFOCUS=&__EVENTTARGET=ctl00%24ContentPlaceHolder1%24GridView1&__EVENTARGUMENT={page_number_encoded}&__VIEWSTATE={view_state}&__VIEWSTATEGENERATOR=0AF47E56&__VIEWSTATEENCRYPTED=&__EVENTVALIDATION={event_validation}&__ASYNCPOST=true&"
        response = requests.post(
            "https://www.cclerk.hctx.net/Applications/WebSearch/FRCL_R.aspx",
            headers=CClerkCrawlerConstants.headers.value,
            data=data,
        )
        # Save raw response
        with open(os.path.join(RAW_RESPONSES, f"page_{page_number}.html"), "wb") as f:
            f.write(response.text.encode("utf-8"))
        if response.status_code == 200:
            _logger.info(f"Successfully fetched page {page_number}.")
            return response
        else:
            _logger.error(
                f"Failed to fetch page {page_number}. Status code: {response.status_code}"
            )
            return False

    def snake_to_title(self, snake_str: str) -> str:
        """
        Converts a snake_case string to a title case string.

        Args:
            snake_str (str): The snake_case string.

        Returns:
            str: The title case string.
        """
        return snake_str.replace("_", " ")

    def parse_data(self, data):
        _logger.info("Parsing data for ValidateData model...")
        data_model = ValidateData(
            file_name=data.get("file_name", ""),
            pdf_url=data.get("pdf_url", ""),
            record_id=data.get("record_id", ""),
        )
        _logger.info(f"Data Validated Successfully: {data_model}")
        return data_model


def main():
    STATUS = True
    pages_available = True
    page_number = 2
    month = 4

    c_clerk_manager = CClerkCrawler()

    # Handle Pagination Logic..
    CClerkCrawlerConstants.data.value["__EVENTARGUMENT"] = f"Page%24{page_number}"
    home_page_response = c_clerk_manager.home_page_request()
    if not home_page_response:
        STATUS = False
        return STATUS

    c_clerk_manager.get_view_state_and_event_validation(home_page_response)

    pdf_hrefs, document_names = c_clerk_manager.extract_doclinks(home_page_response)
    if not pdf_hrefs:
        STATUS = False
        return STATUS
    
    while pages_available:
        for pdf_href, doc_name in zip(pdf_hrefs, document_names):
            _logger.info(f"Processing PDF Link: {pdf_href}")
            data = {
                "record_id": str(uuid4()),
                "file_name": doc_name,
                "pdf_url": f"https://www.cclerk.hctx.net/Applications/WebSearch/{pdf_href}",
            }
            data_model = c_clerk_manager.parse_data(data)
            model_dict = data_model.model_dump()
            data_dict = {
                c_clerk_manager.snake_to_title(key): value
                for key, value in model_dict.items()
            }
            c_clerk_manager.airtable_manager.upsert(data=data_dict)
            _logger.info(f"Parsed Data: {data_model}")

            # Download and save PDF here
            pdf_download_status = c_clerk_manager.download_pdf(pdf_href)
            if not pdf_download_status:
                _logger.error(f"Failed to download PDF for {pdf_href}.")
                STATUS = False
                continue

            file_name = f"{doc_name.replace('-', '_')}.pdf"
            pdf_save_status = c_clerk_manager.save_pdf(pdf_download_status, file_name)
            if not pdf_save_status:
                _logger.error(f"Failed to save PDF for {pdf_href}.")
                STATUS = False
                continue

        # Check if there are more pages
        next_page_data = c_clerk_manager.get_next_page_data(page_number, month)
        if not next_page_data:
            pages_available = False
            _logger.info("No more pages available or failed to fetch next page data.")

        pdf_hrefs, document_names = c_clerk_manager.extract_doclinks(next_page_data)
        page_number += 1
