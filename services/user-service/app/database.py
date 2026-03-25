from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://admin:admin123@postgres:5432/microservices_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)