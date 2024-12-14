# app/main.py
from fastapi import FastAPI
from app.routes import recipes, mealplans
from app.database import create_database
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

create_database()

# Initialize FastAPI app
app = FastAPI()

# Include routes for recipes and meal plans
app.include_router(recipes.router, prefix="/api/recipes")
app.include_router(mealplans.router, prefix="/api/mealplans")