from fastapi import FastAPI
from .database import engine, Base
from .api.v1.endpoints import router as api_router

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="Uma API RESTful simples para gerenciamento de tarefas, construída com FastAPI e SQLite.",
    version="1.0.0",
)

# Inclui as rotas da API
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à Task Manager API. Acesse /docs para a documentação interativa."}

