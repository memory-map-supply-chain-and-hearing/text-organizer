from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from routes import tests

app = FastAPI()

# Reference: https://fastapi.tiangolo.com/tutorial/bigger-applications/
router = APIRouter(prefix="/api/v1")
router.include_router(tests.router, prefix="/tests")

app.include_router(router)

# This defines what "data" the server expects to receive
class DocRequest(BaseModel):
    id: str

@app.get("/")
def server_up():
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
