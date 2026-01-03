from fastapi import FastAPI
from app.database import Base, engine
from app.routers import books

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Management API")

app.include_router(books.router)
