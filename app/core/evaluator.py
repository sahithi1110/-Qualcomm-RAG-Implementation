import json
from pathlib import Path

from app.core.config_loader import load_settings
from app.core.rag_service import RAGService


def run_evaluation() -> dict:
    settings = load_settings()
    evaluation_file = Path(settings["paths"]["evaluation_file"])

    with evaluation_file.open("r", encoding="utf-8") as file:
        questions = json.load(file)

    service = RAGService()

    total = len(questions)
    hits = 0
    detailed_results = []

    for item in questions:
        result = service.ask(item["question"])
        retrieved_sources = set(result["sources"])
        expected_source = item["expected_source"]
        hit = expected_source in retrieved_sources

        hits += int(hit)

        detailed_results.append(
            {
                "question": item["question"],
                "expected_source": expected_source,
                "retrieved_sources": sorted(retrieved_sources),
                "hit": hit,
            }
        )

    hit_rate = hits / total if total else 0

    output = {
        "total_questions": total,
        "successful_hits": hits,
        "retrieval_hit_rate": round(hit_rate, 4),
        "retrieval_hit_rate_percent": f"{hit_rate:.2%}",
        "results": detailed_results,
    }

    output_file = Path(settings["paths"]["evaluation_output_file"])
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(json.dumps(output, indent=2), encoding="utf-8")

    return output
