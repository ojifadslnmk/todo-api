from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine

app = FastAPI()


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Todo API is running"}
