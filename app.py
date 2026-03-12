from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(title="Practice Project for Git hey ayush")

@app.get("/")
def root():
    return RedirectResponse("/docs")