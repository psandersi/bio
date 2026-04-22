from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import tasks, assistant, progress

app = FastAPI(title="BioOlymp AI", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks.router, prefix="/api/tasks", tags=["tasks"])
app.include_router(assistant.router, prefix="/api/assistant", tags=["assistant"])
app.include_router(progress.router, prefix="/api/progress", tags=["progress"])


@app.get("/api/health")
def health():
    return {"status": "ok"}
