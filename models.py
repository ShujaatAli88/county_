from pydantic import BaseModel

class ValidateData(BaseModel):
    record_id: str
    file_name: str
    pdf_url: str