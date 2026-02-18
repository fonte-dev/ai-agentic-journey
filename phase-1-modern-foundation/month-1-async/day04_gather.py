import asyncio
import time


async def boil_water():
    print("💧 Starting to boil water...")
    await asyncio.sleep(2)
    print("🔥 Water is boiling!")
    return "Hot Water"


async def chop_vegetables():
    print("🔪 Starting to chop vegetables...")
    await asyncio.sleep(3)
    print("🥕 Vegetables are chopped!")
    return "Chopped Veggies"


async def cook_meat():
    print("🥩 Starting to cook meat...")
    await asyncio.sleep(4)
    print("🍖 Meat is cooked!")
    return "Cooked Meat"


async def main():
    start_time = time.time()

    print("🚀 Kitchen is open! Starting all tasks...")

    # THE MAGIC MOMENT:
    # asyncio.gather() schedules all these tasks on the Event Loop at the same time.
    # It returns a list of results in the same order you passed them.
    results = await asyncio.gather(boil_water(), chop_vegetables(), cook_meat())

    # Unpacking the results list into variables
    water, veggies, meat = results

    end_time = time.time()
    total_time = end_time - start_time

    print(f"\n🍽️  Dinner is served!")
    print(f"Items prepared: {water}, {veggies}, {meat}")
    print(f"⏱️  Total time taken: {total_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
