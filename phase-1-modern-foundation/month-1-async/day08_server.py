# Day 8 - HTTP Requests
# Learning goal: The Agent's ability to reach the outside world.
# Date: Feb 2026
# Status: Done ✅

import asyncio
from fastapi import FastAPI
import uvicorn
import random

# 1. Initialize the App
app = FastAPI()


# 2. Define a generic root endpoint
@app.get("/")
async def root():
    return {"message": "System Online"}


# 3. Define the "Slow" Endpoint
# This simulates a database query that takes 2 seconds per request.
@app.get("/patient/{patient_id}")
async def get_patient_data(patient_id: int):
    print(f"Server: Received request for Patient {patient_id}...")

    # 1. Simulate a random crash (20% chance)
    if random.random() < 0.2:
        print(f"Server: 💥 CRASHED on Patient {patient_id}!")
        # 500 = Internal Server Error
        # In FastAPI, we can just raise an exception to simulate this
        from fastapi import HTTPException

        raise HTTPException(status_code=500, detail="Random Server Explosion")

    # 2. Simulate delay (Normal behavior)
    await asyncio.sleep(2)

    print(f"Server: Finished Patient {patient_id}.")
    return {
        "id": patient_id,
        "status": "active",
        "notes": f"Therapy session notes for patient {patient_id}...",
    }


# 4. Run the server
if __name__ == "__main__":
    # We use uvicorn to run the FastAPI app
    print("Starting server on http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
