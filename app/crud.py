from sqlalchemy.orm import Session
from app.models import ChatHistory

def listar(db: Session):
    return db.query(ChatHistory).all()

def buscar(db: Session, chat_id: int):
    return db.query(ChatHistory).filter(ChatHistory.id == chat_id).first()

def criar(db: Session, pergunta: str, resposta: str):
    chat = ChatHistory(pergunta=pergunta, resposta=resposta)
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat

def atualizar(db: Session, chat_id: int, pergunta: str, resposta: str):
    chat = buscar(db, chat_id)
    if chat:
        chat.pergunta = pergunta
        chat.resposta = resposta
        db.commit()
        db.refresh(chat)
    return chat

def remover(db: Session, chat_id: int):
    chat = buscar(db, chat_id)
    if chat:
        db.delete(chat)
        db.commit()
        return True
    return False
