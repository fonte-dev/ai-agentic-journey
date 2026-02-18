import asyncio
import httpx


async def manual_lifecycle():
    print("--- STARTING MANUAL MODE ---")

    # 1. Open the browser (Manually)
    client = httpx.AsyncClient()
    print("🔓 Client opened manually.")

    try:
        # 2. Do some work (We will simulate a crash here)
        print("⚡ Doing risky work...")
        raise ValueError("Oops! Something broke!")

        # 3. Close the browser (This line will NEVER run)
        await client.aclose()
        print("🔒 Client closed.")

    except ValueError as e:
        print(f"💥 Caught error: {e}")
        # The client is still open here! We forgot to close it in the except block.


async def main():
    await manual_lifecycle()

    # We sleep briefly to let Python realize the mistake
    await asyncio.sleep(1)
    print("\n❓ Is the client closed? We don't know (it's leaked).")
    print("You might see a 'Unclosed client session' warning below.")


if __name__ == "__main__":
    asyncio.run(main())
