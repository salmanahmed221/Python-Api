from fastapi import FastAPI

app:FastAPI = FastAPI()

@app.get("/hi")
def get_name(name:str,age:int):
    return {"name":name,"age":age}