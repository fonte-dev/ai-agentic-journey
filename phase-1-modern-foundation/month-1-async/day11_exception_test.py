import asyncio
import httpx


async def fetch_url(client, url):
    print(f"🔵 Fetching: {url}")
    # NO try/except here! We are "letting it crash".
    resp = await client.get(url)
    return resp.status_code


async def main():
    urls = [
        "https://www.google.com",
        "https://this-url-does-not-exist.com",  # <--- This will crash
        "https://www.github.com",
    ]

    async with httpx.AsyncClient() as client:
        tasks = [fetch_url(client, url) for url in urls]

        print("--- Starting Gather (with return_exceptions=True) ---")

        # This is the specific feature from the syllabus:
        results = await asyncio.gather(*tasks, return_exceptions=True)

        print("\n--- Results Analysis ---")
        for i, result in enumerate(results):
            # We can check if the result is an actual Error Object
            if isinstance(result, Exception):
                print(f"❌ Task {i} Failed with error: {result}")
            else:
                print(f"✅ Task {i} Succeeded: Status {result}")


if __name__ == "__main__":
    asyncio.run(main())
