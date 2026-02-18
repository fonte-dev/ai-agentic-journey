import asyncio
import httpx


async def safe_lifecycle():
    print("--- STARTING SAFE MODE ---")

    # The "Guard Rail"
    async with httpx.AsyncClient() as client:
        print("🔓 Client opened automatically.")

        print("⚡ Doing risky work...")
        raise ValueError("Oops! Something broke!")

        # We don't need to write 'await client.aclose()'.
        # Python guarantees it happens when we leave this indentation block.


async def main():
    try:
        await safe_lifecycle()
    except ValueError:
        print("💥 Caught error outside.")

    print("\n✅ Client is definitely closed. No leaks.")


if __name__ == "__main__":
    asyncio.run(main())
