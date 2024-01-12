from fastapi import FastAPI, Depends

app = FastAPI()

# the dependency function:
def user_dep(name: str = None, password: str = None): 
    return {"name": name, "password": password}

# the path function / web endpoint:
@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user