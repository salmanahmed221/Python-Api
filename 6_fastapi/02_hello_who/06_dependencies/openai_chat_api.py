import openai
from fastapi import FastAPI, Depends
from typing import Annotated


openai.api_key = ""  # Set your OpenAI API key here

def chat_completion(prompt: str) -> str | None:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    return response['choices'][0]['message']['content']

app:FastAPI = FastAPI()

@app.get("/chat/{prompt}")
def add_data(prompt: Annotated[str, Depends(chat_completion)]):
    return {"openai": prompt}
