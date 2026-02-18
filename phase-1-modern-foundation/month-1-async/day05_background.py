# Day 5 - Background Tasks
# Learning goal: Parallelism concept: Monitoring a patient while filling paperwork.
# Date: Feb 2026
# Status: Done ✅

import asyncio


async def heartbeat():
    # This runs forever!
    while True:
        print("💓 Beep (Heartbeat)")
        await asyncio.sleep(1)


async def long_process():
    print("Beginning heavy download...")
    # Simulate a long task (5 seconds)
    await asyncio.sleep(5)
    print("Download complete!")


async def main():
    print("--- STARTING ---")

    # 1. Start the heartbeat in the background.
    # We do NOT 'await' it here. If we did, we'd be stuck in the while True loop forever.
    # asyncio.create_task() schedules it to run on the loop ASAP.
    background_task = asyncio.create_task(heartbeat())

    # 2. Immediately start the main work.
    # While this 'awaits' the 5 second sleep, the Event Loop is free
    # to run the 'heartbeat' task during the idle time.
    await long_process()

    # 3. Clean up.
    # Since heartbeat() runs forever, we have to manually stop it.
    print("--- FINISHED ---")
    background_task.cancel()

    # Optional: Wait for it to actually cancel (avoids a warning)
    try:
        await background_task
    except asyncio.CancelledError:
        print("Heartbeat stopped.")


if __name__ == "__main__":
    asyncio.run(main())
