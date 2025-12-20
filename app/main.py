from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
import os

from app.routers import chats, history
from app.database import Base, engine
from app import crud
from app.openai_chat import perguntar_openai

# Cria as tabelas no banco (se não existirem)
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="API Externa - ChatJarvis"
)


@app.get("/")
def root():
    return {
        "message": "API externa rodando 🚀",
        "env": os.getenv("ENV"),
        "app_name": os.getenv("APP_NAME")
    }


# Registra os routers
app.include_router(chats.router)
app.include_router(history.router)