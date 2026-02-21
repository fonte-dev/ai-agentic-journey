# Day 18 - Async Queues (The Triage System)
# Task: Async Queues: Use asyncio.Queue. Producer (Client) -> Queue -> Consumer (Server).
# Learning goal: Buffering inputs (Triage queue).
# Date: Feb 2026
# Status: Done ✅

import asyncio
import random


async def producer(queue, producer_id):
    """The Ambulance: Drops off patients into the waiting room at random times."""
    for i in range(1, 4):
        patient_name = f"Patient {i} (from Ambulance {producer_id})"

        # Simulate time it takes for an ambulance to arrive
        await asyncio.sleep(random.uniform(0.5, 1.5))

        # PUT the patient in the queue
        await queue.put(patient_name)
        print(
            f"🚑 Ambulance {producer_id} dropped off: {patient_name}. (Waiting room size: {queue.qsize()})"
        )


async def consumer(queue, doctor_id):
    """The Doctor: Takes patients from the waiting room and treats them."""
    while True:
        # GET a patient from the queue.
        # If the queue is empty, the doctor just waits (sleeps) here automatically!
        patient = await queue.get()
        print(f"👨‍⚕️ Doctor {doctor_id} is treating: {patient}")

        # Simulate the time it takes to treat the patient (Doctors are slower than ambulances)
        await asyncio.sleep(random.uniform(1.0, 2.5))
        print(f"✅ Doctor {doctor_id} finished treating: {patient}")

        # Tell the queue that this specific task is 100% complete
        queue.task_done()


async def main():
    # 1. Create the Waiting Room (Queue)
    # You can set a maxsize (e.g., maxsize=5). If full, producers wait outside.
    waiting_room = asyncio.Queue()

    # 2. Start the Consumers (Doctors)
    # We hire 2 doctors. They run in the background forever.
    doctors = []
    for i in range(1, 3):
        task = asyncio.create_task(consumer(waiting_room, i))
        doctors.append(task)

    # 3. Start the Producers (Ambulances)
    # 3 ambulances are bringing patients in.
    ambulances = []
    for i in range(1, 4):
        ambulances.append(producer(waiting_room, i))

    # 4. Wait for all ambulances to finish dropping off patients
    await asyncio.gather(*ambulances)
    print("\n--- 🛑 All ambulances have finished dropping off patients! ---\n")

    # 5. Wait for the waiting room to completely empty out
    # .join() blocks the program until every item put in the queue has a matching .task_done()
    await waiting_room.join()
    print("--- 🏥 Waiting room is empty. All patients treated! ---")

    # 6. Send the doctors home (Cancel their infinite loops)
    for doc in doctors:
        doc.cancel()


if __name__ == "__main__":
    asyncio.run(main())
