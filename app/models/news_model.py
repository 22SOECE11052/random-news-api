from pydantic import BaseModel

class NewsResponse(BaseModel):
    headline: str
    category: str
    sentiment: str
