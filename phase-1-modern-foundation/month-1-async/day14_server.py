# Day 14 - Async Scraper (Server)
# Learning goal: Master asyncio.gather(), httpx, and file I/O with async
# Date: Feb 2026
# Status: Working ✅

import asyncio
import random
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()


@app.get("/record/{id}", response_class=HTMLResponse)
async def get_record(id: int):
    # 1. Simulate "Hanging" (Timeout Test)
    # 5% chance the server hangs for 10 seconds
    if random.random() < 0.05:
        await asyncio.sleep(10)

    # 2. Simulate "Crashing" (Retry Test)
    # 10% chance of Internal Server Error
    if random.random() < 0.10:
        raise HTTPException(status_code=500, detail="Database Connection Failed")

    # 3. Normal Slow Response
    delay = random.uniform(0.5, 2.0)
    await asyncio.sleep(delay)

    # 4. The HTML Content (Parsing Test)
    names = ["Sarah", "John", "Kyle", "Terminator", "Ellen", "Ripley"]
    conditions = ["Stable", "Critical", "Discharged", "Deceased", "Unknown"]

    html = f"""
    <html>
        <div class="patient-card">
            <h1>Patient Record #{id}</h1>
            <div class="details">
                <span class="name">Name: {random.choice(names)}</span>
                <span class="condition">Condition: {random.choice(conditions)}</span>
            </div>
        </div>
    </html>
    """
    return html


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
