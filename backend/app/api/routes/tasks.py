from fastapi import APIRouter, HTTPException
from app.models.task import Task, AnswerSubmit, AnswerResult

router = APIRouter()

# Placeholder data - replace with DB later
TASKS: list[Task] = [
    Task(
        id=1,
        topic="Клетка",
        difficulty="medium",
        question="Какова функция митохондрий в клетке?",
        correct_answer="Синтез АТФ (клеточное дыхание)",
        explanation="Митохондрии - энергетические станции клетки. Они производят АТФ через процесс клеточного дыхания.",
    )
]


@router.get("/", response_model=list[Task])
def get_tasks(topic: str | None = None):
    if topic:
        return [t for t in TASKS if t.topic == topic]
    return TASKS


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = next((t for t in TASKS if t.id == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("/submit", response_model=AnswerResult)
def submit_answer(body: AnswerSubmit):
    task = next((t for t in TASKS if t.id == body.task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    is_correct = body.user_answer.strip().lower() == task.correct_answer.lower()
    return AnswerResult(
        is_correct=is_correct,
        correct_answer=task.correct_answer,
        explanation=None if is_correct else task.explanation,
        recommended_topic=None if is_correct else task.topic,
    )
