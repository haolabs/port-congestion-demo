# port-congestion-demo
![Python CI](https://github.com/haolabs/port-congestion-demo/actions/workflows/python.yml/badge.svg)

Minimal FastAPI baseline that reads a small CSV and returns a numeric prediction.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

## Endpoints
	•	GET /health → {"ok": true}
	•	GET /predict?port=LA&date=2026-06-01 → numeric prediction
	•	Swagger: http://127.0.0.1:8000/docs

## Example
curl 'http://127.0.0.1:8000/health'
curl 'http://127.0.0.1:8000/predict?port=LA&date=2026-06-01'

