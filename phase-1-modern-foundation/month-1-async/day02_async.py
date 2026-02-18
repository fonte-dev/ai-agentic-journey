# Day 2 - AsyncIO
# Learning goal: Non-blocking syntax.
# Date: Feb 2026
# Status: Done ✅

import asyncio


# 1. We define a coroutine with 'async def'
async def main():
    print("Hello")

    # 2. We PAUSE here using 'await'.
    # Unlike time.sleep(), this doesn't freeze the computer.
    # It tells the Event Loop: "I'm busy waiting for 2 seconds. Go do other work."
    await asyncio.sleep(2)

    print("World")


if __name__ == "__main__":
    # 3. We can't just call main() anymore because it's a coroutine.
    # We need a "runner" to start the Event Loop and run our task.
    asyncio.run(main())
