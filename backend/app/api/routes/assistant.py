from fastapi import APIRouter
from app.models.assistant import QuestionRequest, QuestionResponse

router = APIRouter()


@router.post("/ask", response_model=QuestionResponse)
async def ask_question(body: QuestionRequest):
    # TODO: replace with GigaChat / YandexGPT + RAG
    return QuestionResponse(
        answer=f"[AI placeholder] Вопрос получен: {body.question}",
        source=None,
    )
