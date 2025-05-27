from config import Config
from constants import AirtableConstants
from log_handler import _logger
from pyairtable import Api

class AirtableManager:
    def __init__(self):
        self.base_id = Config.AIRTABLE_BASE_ID
        self.table_name = AirtableConstants.airtable_name.value
        self.api_key = self.api = Api(api_key=Config.AIRTABLE_API_KEY)
        self.endpoint = f"https://api.airtable.com/v0/{self.base_id}/{self.table_name}"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def upsert(self, *, data):
        _logger.info("Upserting records into Air Table.")
        table = self.api_key.table(
            base_id=self.base_id, 
            table_name=AirtableConstants.airtable_name.value
        )
        table.batch_upsert(records=[dict(fields=data)], key_fields=["record id"])
        _logger.info("Records Upserted Successfully.")