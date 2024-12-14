# app/routes/mealplans.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, models, database

router = APIRouter()

@router.post("/create")
def create_mealplan(date: str, meal_ids: str, db: Session = Depends(database.SessionLocal)):
    return crud.create_mealplan(db, date, meal_ids)