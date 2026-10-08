from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(title="Document Insight App")


class DocumentRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return FileResponse("index.html")


@app.post("/analyze")
def analyze_document(document: DocumentRequest):
    text = document.text

    return {
        "characters": len(text),
        "words": len(text.split()),
        "lines": len(text.splitlines())
    }