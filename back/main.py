import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from match import compute_match
from schemas import MatchRequest, MatchResponse

ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:5173,http://127.0.0.1:5173"
).split(",")

_docs = os.getenv("ENABLE_DOCS", "false").lower() == "true"

app = FastAPI(
    title="My Portfolio API",
    docs_url="/docs" if _docs else None,
    redoc_url=None,
    openapi_url="/openapi.json" if _docs else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI 🎉"}

@app.post("/match", response_model=MatchResponse)
def match(payload: MatchRequest):
    return compute_match(payload)