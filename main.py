import uvicorn
from fastapi import FastAPI, Request, Form
from config import load_env, ModelType
from igcy_chatbot import setup_llm
from typing import List
from igcy_chatbot.models import Message

load_env()

app = FastAPI()

llm = setup_llm()

@app.get("/")
def read_root(request: Request):
    return {"message": "Welcome Fox Chatbot"}


@app.post("/prompt")
def process_prompt(messages: List[Message]):
    response = llm.ask(query_type="test", messages=messages, model_type=ModelType.gpt4o)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)