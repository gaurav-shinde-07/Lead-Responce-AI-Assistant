from pydantic import BaseModel

class IntentSchema(BaseModel):
    intent: str

class ExtractionSchema(BaseModel):
    location: str
    trigger: str
    visible_sign: str
    duration: str
