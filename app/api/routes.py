from fastapi import APIRouter

from app.core.evaluator import run_evaluation
from app.core.rag_service import RAGService
from app.models.schemas import QuestionRequest, QuestionResponse


router = APIRouter()
service = RAGService()


@router.get("/")
def health_check() -> dict:
    return {
        "status": "running",
        "message": "Enterprise RAG LLM Quality Evaluation API is active",
    }


@router.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest) -> dict:
    return service.ask(request.question)


@router.get("/sources")
def list_sources() -> dict:
    return service.list_sources()


@router.get("/evaluate")
def evaluate_project() -> dict:
    return run_evaluation()
