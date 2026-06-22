from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="Enterprise RAG LLM Quality Evaluation",
    description="A sanitized RAG project for grounded answers, retrieval quality, and AI response evaluation.",
    version="1.0.0",
)

app.include_router(router)
