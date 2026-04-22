from pydantic import BaseModel
from typing import Optional
from enum import Enum


class Difficulty(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"


class Task(BaseModel):
    id: int
    topic: str
    difficulty: Difficulty
    question: str
    correct_answer: str
    explanation: str


class AnswerSubmit(BaseModel):
    task_id: int
    user_answer: str


class AnswerResult(BaseModel):
    is_correct: bool
    correct_answer: str
    explanation: Optional[str] = None
    recommended_topic: Optional[str] = None
