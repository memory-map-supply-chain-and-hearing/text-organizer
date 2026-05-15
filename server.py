from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# This defines what "data" the server expects to receive
class DocRequest(BaseModel):
    id: str

@app.get("/")
def read_root():
    return {"status": "Backend is running"}

@app.post("/process-doc")
def process_doc(request: DocRequest):
    # This is where we will eventually put the Google Docs logic.
    # For now, it just confirms it received the ID.
    print(f"Received request to process Google Doc ID: {request.id}")
    return {
        "message": f"Successfully received Doc ID: {request.id}",
        "status": "received"
    }
