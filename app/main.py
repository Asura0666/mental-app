from fastapi import FastAPI
# from app.routers import item
from app.database.database import engine
# from app.models.item import Base

# Initialize the database tables if not done already
# Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI!"}

# Include routes
# app.include_router(item.router)


