# Day 11 - Error Handling
# Learning goal: Resilience: Ensuring one failure doesn't crash the whole application.
# Date: Feb 2026
# Status: Done ✅

import asyncio
import httpx
import time


async def get_patient_with_retry(client, patient_id, semaphore, max_retries=3):
    async with semaphore:
        for attempt in range(1, max_retries + 1):
            url = f"http://127.0.0.1:8000/patient/{patient_id}"

            try:
                # We try to get the data
                resp = await client.get(url, timeout=10.0)

                # Check if the status code is 200 (OK).
                # If it's 500, this line raises an error.
                resp.raise_for_status()

                print(f"🟢 Received Patient {patient_id}")
                return resp.json()

            except httpx.HTTPStatusError as e:
                print(f"⚠️  Error on Patient {patient_id} (Attempt {attempt}): {e}")
                if attempt == max_retries:
                    print(
                        f"❌ FAILED Patient {patient_id} after {max_retries} attempts."
                    )
                    return None  # Give up

                # Wait a bit before retrying (Exponential Backoff is better, but simple sleep works)
                await asyncio.sleep(1)


async def main():
    patient_ids = range(1, 21)  # Let's do 20 patients
    sem = asyncio.Semaphore(5)

    async with httpx.AsyncClient() as client:
        tasks = []
        for p_id in patient_ids:
            tasks.append(get_patient_with_retry(client, p_id, sem))

        results = await asyncio.gather(*tasks)

    # Count successes
    success_count = len([r for r in results if r is not None])
    print(f"\n--- DONE: {success_count}/{len(patient_ids)} successful ---")


if __name__ == "__main__":
    asyncio.run(main())
