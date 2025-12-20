from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/history", tags=["Histórico"])

@router.get("/", response_model=list[schemas.ChatResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar(db)

@router.get("/{chat_id}", response_model=schemas.ChatResponse)
def buscar(chat_id: int, db: Session = Depends(get_db)):
    chat = crud.buscar(db, chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    return chat

@router.put("/{chat_id}", response_model=schemas.ChatResponse)
def atualizar(chat_id: int, data: schemas.ChatUpdate, db: Session = Depends(get_db)):
    chat = crud.atualizar(db, chat_id, data.pergunta, data.resposta)
    if not chat:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    return chat

@router.delete("/{chat_id}")
def remover(chat_id: int, db: Session = Depends(get_db)):
    sucesso = crud.remover(db, chat_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    return {"status": "Removido com sucesso"}
