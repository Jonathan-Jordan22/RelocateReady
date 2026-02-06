from fastapi import FastAPI

app = FastAPI(title="RelocateReady")

@app.get("/")
def health_check():
    return {"status": "RelocateReady API is running"}