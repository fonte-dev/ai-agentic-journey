# Day 6 - Blocking the Loop
# Learning goal: Understanding how one blocking action freezes the whole system.
# Date: Feb 2026
# Status: Done ✅

import asyncio
import time  # <--- The enemy


async def heartbeat():
    while True:
        print("💓 Beep")
        await asyncio.sleep(1)


async def long_process():
    print("Beginning heavy download...")

    # FATAL MISTAKE:
    # We use time.sleep(5) instead of await asyncio.sleep(5).
    # This captures the CPU and REFUSES to let go.
    # No 'await' means no switching.
    time.sleep(5)

    print("Download complete!")


async def main():
    # Start the heartbeat
    task = asyncio.create_task(heartbeat())

    # Run the blocker
    print("--- STARTING BLOCKING TASK ---")
    await long_process()
    print("--- FINISHED BLOCKING TASK ---")

    task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
