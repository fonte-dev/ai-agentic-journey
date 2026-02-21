# Day 14 - Async Patient Record Scraper (Agent)
# Learning goal: Master asyncio.gather(), httpx, resilience patterns and async file I/O
# Date: Feb 2026
# Status: Done ✅

# What this project demonstrates:
# • Concurrency: 100 requests with Semaphore(10) → no DDOS
# • Resilience: Automatic retries (3 attempts) on 500 errors
# • Timeout protection: asyncio.wait_for(3 seconds)
# • HTML parsing: BeautifulSoup + safe extraction
# • Persistence: Results saved to patients.csv
# • Domain relevance: Patient records (direct practice for MERITUM)

import asyncio
import httpx
from bs4 import BeautifulSoup


def safe_extract(element, tag_name: str, class_name: str) -> str:
    """Safely extract text from HTML element or return 'Unknown'."""
    found = element.find(tag_name, class_=class_name)
    return found.text.strip() if found else "Unknown"


def parse_patient(html: str, patient_id: int) -> dict:
    """Extract name and condition from HTML response."""
    soup = BeautifulSoup(html, "html.parser")
    name = safe_extract(soup, "span", "name")
    condition = safe_extract(soup, "span", "condition")
    return {"id": patient_id, "name": name, "condition": condition}


async def fetch_patient(
    client: httpx.AsyncClient,
    patient_id: int,
    semaphore: asyncio.Semaphore,
    max_retries: int = 3,
):
    async with semaphore:
        for attempt in range(1, max_retries + 1):
            try:
                url = f"http://127.0.0.1:8000/record/{patient_id}"
                print(f"Requesting Patient {patient_id} (attempt {attempt})")

                resp = await asyncio.wait_for(client.get(url), timeout=3.0)
                resp.raise_for_status()

                result = parse_patient(resp.text, patient_id)
                print(f"Patient {patient_id} OK")
                return result

            except httpx.HTTPStatusError as e:
                print(
                    f"Error {patient_id} (attempt {attempt}): {e.response.status_code}"
                )
                if attempt == max_retries:
                    print(f"FAILED Patient {patient_id} after {max_retries} attempts")
                    return None
                await asyncio.sleep(1)

            except asyncio.TimeoutError:
                print(f"TIMEOUT Patient {patient_id} cancelled")
                return None

            except Exception as e:
                print(f"Unexpected error {patient_id}: {e}")
                return None


async def main():
    patient_ids = range(1, 101)
    sem = asyncio.Semaphore(10)

    print(f"Starting async scrape of {len(patient_ids)} patients (10 at a time)...\n")

    async with httpx.AsyncClient() as client:
        tasks = [fetch_patient(client, pid, sem) for pid in patient_ids]
        results = await asyncio.gather(*tasks)

    with open("patients.csv", "w", encoding="utf-8") as f:
        f.write("ID,Name,Condition\n")
        for result in results:
            if result:
                name_clean = result["name"].replace("Name: ", "").strip()
                cond_clean = result["condition"].replace("Condition: ", "").strip()
                f.write(f"{result['id']},{name_clean},{cond_clean}\n")

    print("\nScrape finished! Results saved to patients.csv")


if __name__ == "__main__":
    asyncio.run(main())
