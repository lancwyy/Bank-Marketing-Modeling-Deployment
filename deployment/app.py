from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the trained pipeline
model = joblib.load("xgb_pipeline_v1.joblib")

# Define input schema
class InputData(BaseModel):
    age: float
    balance: float
    duration: float
    campaign: float
    previous: float
    date: int
    month: int
    poutcome: str
    contact: str
    housing: bool
    loan: bool
    default: bool
    job: str
    education: str
    marital: str

app = FastAPI()

@app.post("/predict")
def predict(data: InputData):
    try:
        input_df = pd.DataFrame([data.model_dump()])
        pred = int(model.predict(input_df)[0])
        prob = float(model.predict_proba(input_df)[0][1])
        return {
            "prediction": int(pred),
            "probability": round(prob, 4)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
