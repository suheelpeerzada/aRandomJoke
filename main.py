#fastAPI import here
#runs server
from fastapi import FastAPI, APIRouter
from app.api import route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(route) #router is attached here

@app.get("/test")
def test():
    return {"status": "active"}