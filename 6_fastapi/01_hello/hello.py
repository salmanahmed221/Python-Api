from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get("/") 
def greet():
    return {"text": "Hello World"}

@app.get("/{name}")
def greet_with_name(name: str):
    return "Hello? World, " + name

# print("print",__name__)

if __name__ == "__main__": 
    import uvicorn
    uvicorn.run("hello:app", reload=True)