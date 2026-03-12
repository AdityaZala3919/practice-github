from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(title="Practice Project for Git hey ayush kotadiya")

@app.get("/")
def root(a: str = "Hello World"):
    return RedirectResponse("/docs")