from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# URL do banco de dados - pode ser configurada via variável de ambiente
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://usuario:senha@localhost:5432/nome_do_banco")

# Criar engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Criar sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

# Dependency para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 