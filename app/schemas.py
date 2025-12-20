from pydantic import BaseModel
from datetime import datetime

class ChatCreate(BaseModel):
    message: str

class ChatResponse(BaseModel):
    id: int
    pergunta: str
    resposta: str
    created_at: datetime

    class Config:
        orm_mode = True

class ChatUpdate(BaseModel):
    pergunta: str
    resposta: str
