
# port-congestion-demo

Minimal FastAPI baseline that reads a small CSV and returns a numeric prediction.

## Run locally

1. (Optional) Create a virtualenv
   ```bash
   python -m venv .venv && source .venv/bin/activate
   ```
2. Install deps
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the API
   ```bash
   uvicorn app:app --reload
   ```

## Endpoints

- `GET /health`
- `GET /predict?port=LA&date=2026-06-01` → returns baseline mean

## Notes
- Data lives in `data/sample.csv`.
