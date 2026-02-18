from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.routes import todos

app = FastAPI()
app.include_router(todos.router)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Todo API is running"}
