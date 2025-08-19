from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pickle
import numpy as np
import pandas as pd

# Load model and preprocessing info
with open("diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("medians.pkl", "rb") as f:
    medians = pickle.load(f)

app = FastAPI()

# Mount static (CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    Pregnancies: int = Form(...),
    Glucose: float = Form(...),
    BloodPressure: float = Form(...),
    SkinThickness: float = Form(...),
    Insulin: float = Form(...),
    BMI: float = Form(...),
    DiabetesPedigreeFunction: float = Form(...),
    Age: int = Form(...)
):
    # Convert form data into dataframe row
    input_data = {
        "Pregnancies": Pregnancies,
        "Glucose": Glucose,
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
        "Age": Age
    }

    # Replace zeros with medians (like training phase)
    for feature, median in medians.items():
        if input_data[feature] == 0:
            input_data[feature] = median

    df_input = pd.DataFrame([input_data])


    # Predict
    prediction = model.predict(df_input)[0]

    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "result": int(prediction)}
    )

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=7860)