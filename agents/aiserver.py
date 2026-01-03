# server.py
from fastapi import FastAPI
from pydantic import BaseModel
from gpt4all import GPT4All  # adjust if your import path is different

# Initialize FastAPI
app = FastAPI(title="Local GPT4All API")

# Load the model
model = GPT4All("gpt4all-lora")  # replace with your model file if different

# Request schema
class CompletionRequest(BaseModel):
    prompt: str
    max_tokens: int = 200

# OpenAI-compatible endpoint
@app.post("/v1/completions")
def completions(req: CompletionRequest):
    # Generate text
    output = model.generate(req.prompt, max_tokens=req.max_tokens)
    return {"choices": [{"text": output}]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "server:app",        # module name : app object
        host="localhost",
        port=5000,
        reload=True          # optional, auto-reload on code changes
    )