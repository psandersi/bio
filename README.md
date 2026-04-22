# BioOlymp AI API

A small FastAPI MVP for biology olympiad practice.

The API includes practice tasks, answer checking, short explanations,  AI placeholder and a basic progress endpoint.

## Project Structure

```text
backend/
├── app/
│   ├── api/routes/   API routes
│   ├── core/         settings
│   ├── models/       Pydantic models
│   └── main.py       FastAPI app
└── requirements.txt
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

This is early MVP. Tasks and progress are currently stored as placeholders in code. AI endpoint is also a placeholder and will later be connected to a real LLM provider.
