from app.core.rag_service import RAGService
from app.core.evaluator import run_evaluation


def test_evaluation_returns_hit_rate():
    service = RAGService()
    service.build_index()

    result = run_evaluation()

    assert "retrieval_hit_rate_percent" in result
    assert result["total_questions"] > 0
    assert result["successful_hits"] >= 1
