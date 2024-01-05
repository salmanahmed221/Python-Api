from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get("/")
def index() -> dict[str,str]:
    return {"text":"hello world123"}

@app.get("/about")
def index1() -> dict[str,str]:
    return {"text":"hello about"}