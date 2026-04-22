from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_progress():
    # TODO: link to user session / DB
    return {
        "solved": 0,
        "correct": 0,
        "weak_topics": [],
    }
