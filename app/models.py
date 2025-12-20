from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base


class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    pergunta = Column(String, nullable=False)
    resposta = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
