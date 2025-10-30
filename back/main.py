from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="My Portfolio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],   # autorise les méthodes (GET/POST/OPTIONS…)
    allow_headers=["*"],   # autorise les headers (incl. Content-Type)
)

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI 🎉"}
