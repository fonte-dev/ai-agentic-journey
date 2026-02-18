# Day 10 - Semaphores (Rate Limiting)
# Learning goal: Preventing the system from overwhelming external services.
# Date: Feb 2026
# Status: Done ✅

import asyncio
import httpx
import time


async def get_patient(client, patient_id, semaphore):
    # THE BOUNCER:
    # "async with semaphore" will PAUSE here if 5 people are already inside.
    # It waits until someone leaves (exits the block) before letting this one in.
    async with semaphore:
        url = f"http://127.0.0.1:8000/patient/{patient_id}"
        print(f"🔵 Requesting Patient {patient_id} (Inside Club)...")

        # This is the slow part (2 seconds)
        resp = await client.get(url, timeout=10.0)

        print(f"🟢 Received Patient {patient_id} (Leaving Club)!")
        return resp.json()


async def main():
    patient_ids = range(1, 51)  # 50 patients

    # 1. Create the Bouncer (Limit to 5 concurrent tasks)
    sem = asyncio.Semaphore(5)

    print(f"--- STARTING FETCH (Max 5 at a time) ---")
    start_time = time.time()

    async with httpx.AsyncClient() as client:
        tasks = []
        for p_id in patient_ids:
            # We pass the bouncer 'sem' to every function
            tasks.append(get_patient(client, p_id, sem))

        # We still gather() them all!
        # But they won't all run at once because of the lock inside the function.
        await asyncio.gather(*tasks)

    end_time = time.time()
    total_time = end_time - start_time

    print(f"\n⏱️  Total time: {total_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
