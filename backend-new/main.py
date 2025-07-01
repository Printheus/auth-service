from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import Base
from app.database import engine

from app.routers import auth

app = FastAPI()
app.include_router(auth.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def index():
    return "Fuck off"

