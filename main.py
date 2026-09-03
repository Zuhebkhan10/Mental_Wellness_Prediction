import joblib
from fastapi import FastAPI

model=joblib.load("Mental_Wellness_model.pkl")

app=FastAPI()

@app.get('/')
def hello():
    return {"Welcome to the my web"}



