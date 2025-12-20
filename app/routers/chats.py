from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import ChatCreate
from app import crud
from app.openai_chat import perguntar_openai

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/")
def chat(data: ChatCreate, db: Session = Depends(get_db)):
    resposta = perguntar_openai(data.message)
    registro = crud.criar(db, data.message, resposta)
    return {
        "id": registro.id,
        "user": registro.pergunta,
        "bot": registro.resposta
    }
