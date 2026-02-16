from fastapi import FastAPI
from .models import Load
from .engine import evaluate_load

api = FastAPI(title="Load Sanity Checker API")

@api.get("/")
def root():
    return {"status": "Load Sanity Checker running"}

@api.post("/check_load")
def check_load(load: Load):
    return evaluate_load(load)