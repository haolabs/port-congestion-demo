
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from typing import Optional

app = FastAPI(title="Port Congestion Demo", version="0.1.0")
df = pd.read_csv("data/sample.csv")

class PredictResponse(BaseModel):
    port: str
    date: Optional[str] = None
    congestion: float

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/predict", response_model=PredictResponse)
def predict(port: str, date: Optional[str] = None):
    sub = df[df["port"].str.lower() == port.lower()]
    if sub.empty:
        raise HTTPException(status_code=404, detail=f"Unknown port: {port}")
    value = float(sub["congestion"].mean())
    return {"port": port, "date": date, "congestion": round(value, 4)}
