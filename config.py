import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    AIRTABLE_BASE_ID = os.getenv("BASE_ID")
    AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")