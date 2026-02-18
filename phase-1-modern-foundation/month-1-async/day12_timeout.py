# Day 12 - Timeouts
# Learning goal: Boundaries: Setting strict time limits on interactions.
# Date: Feb 2026
# Status: Done ✅

import asyncio
import httpx
import time


async def fetch_patient_strict(patient_id):
    url = f"http://127.0.0.1:8000/patient/{patient_id}"

    async with httpx.AsyncClient() as client:
        print(f"⏳ Requesting Patient {patient_id} (Limit: 1.5s)...")

        try:
            # THE CORE LESSON:
            # We wrap the specific task (client.get) in asyncio.wait_for
            # If 1.5 seconds pass, it raises asyncio.TimeoutError and CANCELS the task.
            response = await asyncio.wait_for(client.get(url), timeout=3)

            return response.json()

        except asyncio.TimeoutError:
            print(f"🛑 TIMEOUT! Patient {patient_id} took too long. Cancelling task.")
            return None

        except Exception as e:
            print(f"❌ Other Error: {e}")
            return None


async def main():
    start = time.time()

    # We try to fetch patient 1
    result = await fetch_patient_strict(1)

    end = time.time()

    print(f"\n--- REPORT ---")
    print(f"Result: {result}")
    print(f"Total Time: {end - start:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
