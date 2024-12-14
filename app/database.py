# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
print(f"DATABASE_URL: {DATABASE_URL}")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable is not set.")

with engine.connect() as connection:
    print("Connection successful!")
    
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Create tables in the database
def create_database():
    Base.metadata.create_all(bind=engine)