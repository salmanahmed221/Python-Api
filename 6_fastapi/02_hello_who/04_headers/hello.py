from fastapi import FastAPI, Header

app = FastAPI()

@app.post("/hi")
def greet(name:str = Header()):
    return f"Hello? {name}?"