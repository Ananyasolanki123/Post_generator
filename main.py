from fastapi import FastAPI,Request

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI running on Render"}

@app.post("/api/form-submit")
async def form_submit(payload: dict):
    print("Received from form:", payload)
    return {"status": "ok", "data": payload}
