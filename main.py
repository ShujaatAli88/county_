from c_clerk_crawler import main as main_c_clerk
from log_handler import _logger

def main():
    _logger.info("Starting CClerk Crawler...")
    status = main_c_clerk()
    if not status:
        _logger.error("CClerk Crawler encountered an error.")
    else:
        _logger.info("CClerk Crawler completed successfully.")

if __name__ == "__main__":
    main()