# app/models.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    ingredients = Column(Text)

class MealPlan(Base):
    __tablename__ = "mealplans"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, index=True)
    meal_ids = Column(Text)  # A string of comma-separated meal ids

    recipes = relationship("Recipe", secondary="mealplan_recipes")

class MealPlanRecipe(Base):
    __tablename__ = "mealplan_recipes"
    mealplan_id = Column(Integer, ForeignKey("mealplans.id"), primary_key=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), primary_key=True)