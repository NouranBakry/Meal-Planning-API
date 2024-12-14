# app/crud.py
from sqlalchemy.orm import Session
from app import models

def create_recipe(db: Session, name: str, description: str, ingredients: str):
    db_recipe = models.Recipe(name=name, description=description, ingredients=ingredients)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def create_mealplan(db: Session, date: str, meal_ids: str):
    db_mealplan = models.MealPlan(date=date, meal_ids=meal_ids)
    db.add(db_mealplan)
    db.commit()
    db.refresh(db_mealplan)
    return db_mealplan