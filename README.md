# BioOlymp AI API

A small FastAPI MVP for biology olympiad practice.

The API includes practice tasks, answer checking, short explanations, a simple AI assistant placeholder, and a basic progress endpoint.

## Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## Project Structure

```text
backend/
├── app/
│   ├── api/routes/   API routes
│   ├── core/         settings
│   ├── models/       Pydantic models
│   └── main.py       FastAPI app
├── .env.example
└── requirements.txt
```

## Run

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

The API runs at `http://localhost:8000`.

## API

- `GET /api/health`
- `GET /api/tasks/`
- `GET /api/tasks/{task_id}`
- `POST /api/tasks/submit`
- `POST /api/assistant/ask`
- `GET /api/progress/`

## Status

This is an early MVP. Tasks and progress are currently stored as placeholders in code. The AI assistant endpoint is also a placeholder and can later be connected to a real LLM provider.
