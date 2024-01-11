from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/hi")
def greet(name:str = Body(embed=True)):
    return f"Hello? {name}?"