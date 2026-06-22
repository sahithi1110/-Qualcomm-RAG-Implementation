from pydantic import BaseModel, Field


class QuestionRequest(BaseModel):
    question: str = Field(..., min_length=3, description="Question asked by the user")


class RetrievedContext(BaseModel):
    source: str
    chunk_number: int
    text: str


class QuestionResponse(BaseModel):
    question: str
    answer: str
    sources: list[str]
    confidence_note: str
    retrieved_context: list[RetrievedContext]
    grounded_prompt: str
