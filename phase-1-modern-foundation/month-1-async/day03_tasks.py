import asyncio
import time


# Function 1: A quick task
async def boil_water():
    print("💧 Starting to boil water...")
    await asyncio.sleep(2)  # Simulating a 2-second task
    print("🔥 Water is boiling!")
    return "Hot Water"


# Function 2: A medium task
async def chop_vegetables():
    print("🔪 Starting to chop vegetables...")
    await asyncio.sleep(3)  # Simulating a 3-second task
    print("🥕 Vegetables are chopped!")
    return "Chopped Veggies"


# Function 3: A slow task
async def cook_meat():
    print("🥩 Starting to cook meat...")
    await asyncio.sleep(4)  # Simulating a 4-second task
    print("🍖 Meat is cooked!")
    return "Cooked Meat"


async def main():
    start_time = time.time()

    # REVIEW THIS CAREFULLY:
    # We are 'awaiting' them one by one.
    # This means we start boiling, WAIT until it's done, then start chopping.
    # The Event Loop is technically capable of multitasking,
    # but we are forcing it to be sequential here.

    result1 = await boil_water()
    result2 = await chop_vegetables()
    result3 = await cook_meat()

    end_time = time.time()
    total_time = end_time - start_time

    print(f"\n🍽️  Dinner is served!")
    print(f"⏱️  Total time taken: {total_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
