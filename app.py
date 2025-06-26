from fastapi import FastAPI, Query
from pydantic import BaseModel
from main import agent  # reusing your existing ReAct agent

app = FastAPI()


class QueryResponse(BaseModel):
    prompt: str
    result: str


@app.get("/")
def root():
    return {"message": "AI assistant is running!"}


@app.get("/query", response_model=QueryResponse)
def query_agent(prompt: str = Query(..., description="Your prompt to the agent")):
    result = agent.query(prompt)
    return {"prompt": prompt, "result": str(result)}
