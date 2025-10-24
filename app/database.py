from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL do banco de dados SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Cria o motor do banco de dados
# check_same_thread é necessário apenas para SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria uma SessionLocal, que será a sessão de banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos de dados
Base = declarative_base()

# Função de utilidade para obter a sessão do banco de dados (Dependency Injection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

