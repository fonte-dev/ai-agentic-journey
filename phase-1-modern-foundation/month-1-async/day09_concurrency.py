# Day 9 - Concurrency at Scale
# Learning goal: Realizing the speed difference (seconds vs milliseconds).
# Date: Feb 2026
# Status: Done ✅

import asyncio
import httpx
import time


async def get_patient(client, patient_id):
    url = f"http://127.0.0.1:8000/patient/{patient_id}"
    print(f"🔵 Requesting Patient {patient_id}...")

    resp = await client.get(url, timeout=10.0)

    print(f"🟢 Received Patient {patient_id}!")
    return resp.json()


async def main():
    # We want to fetch 50 patients (IDs 1 to 50)
    patient_ids = range(1, 51)

    print(f"--- STARTING FETCH OF {len(patient_ids)} PATIENTS ---")
    start_time = time.time()

    # We open ONE session and reuse it (much faster than opening 50 sessions)
    async with httpx.AsyncClient() as client:
        tasks = []
        for p_id in patient_ids:
            # CRITICAL: We do NOT 'await' here.
            # We just create the coroutine object and add it to a list.
            # This is the "Order Ticket", not the "Meal".
            tasks.append(get_patient(client, p_id))

        # Now we fire them all at once.
        # asyncio.gather runs all tasks in the list concurrently.
        results = await asyncio.gather(*tasks)

    end_time = time.time()
    total_time = end_time - start_time

    print(f"\n--- COMPLETED ---")
    print(f"Success: {len(results)} patients fetched.")
    print(f"⏱️  Total time: {total_time:.2f} seconds")

    # Just to prove we got data, print the first one
    print(f"Sample data: {results[0]}")


if __name__ == "__main__":
    asyncio.run(main())
