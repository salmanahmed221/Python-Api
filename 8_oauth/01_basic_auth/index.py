from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="")


app:FastAPI = FastAPI()

@app.get("/")
def read_root(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"message": "Hello World"}