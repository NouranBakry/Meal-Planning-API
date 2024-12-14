# app/routes/recipes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, models, database

router = APIRouter()

@router.post("/")
def create_recipe(name: str, description: str, ingredients: str, db: Session = Depends(database.SessionLocal)):
    return crud.create_recipe(db, name, description, ingredients)