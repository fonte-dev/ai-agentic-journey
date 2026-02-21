# Day 22-30 - Triage Simulation (Month 1 Capstone)
# Learning goal: Master OOP Async, PriorityQueue, graceful shutdown, observability
# Date: February 2026
# Status: COMPLETE ✅

import asyncio
from typing import Literal, cast
import time
import random
from faker import Faker
import logging
import argparse

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S",
)

fake = Faker()

# --- CONFIG ---
SHIFT_DURATION = 15.0
NUM_DOCTORS = 3
ARRIVAL_SPEED_MIN = 1.0
ARRIVAL_SPEED_MAX = 3.0


class Patient:
    def __init__(self, p_id: int, name: str, severity: Literal[1, 2, 3, 4, 5]):
        self.p_id = p_id
        self.name = name
        self.severity = severity
        self.arrival_time: float = time.time()

    def __lt__(self, other):
        return self.severity < other.severity  # Higher severity = higher priority


async def patient_register(queue: asyncio.PriorityQueue, p_id: int):
    name = fake.name()
    severity: Literal[1, 2, 3, 4, 5] = cast(
        Literal[1, 2, 3, 4, 5], random.randint(1, 5)
    )
    patient = Patient(p_id, name, severity)
    await queue.put(patient)
    logging.info(f"→ {patient.name} (ID:{patient.p_id}) arrived | Severity: {severity}")


async def doctor(queue: asyncio.PriorityQueue, doctor_id: int, stats: dict):
    while True:
        patient: Patient = await queue.get()
        wait_time = time.time() - patient.arrival_time

        logging.info(
            f"Doctor {doctor_id} treating {patient.name} (Severity {patient.severity}) | Waited {wait_time:.1f}s"
        )

        treatment_time = {1: 5.0, 2: 4.0, 3: 3.0, 4: 2.0, 5: 1.0}[patient.severity]
        await asyncio.sleep(treatment_time)

        total_time = time.time() - patient.arrival_time
        logging.info(
            f"Doctor {doctor_id} discharged {patient.name} in {total_time:.1f}s total"
        )

        # Update stats
        stats["total_patients"] += 1
        stats["wait_times"].append(wait_time)
        stats["total_times"].append(total_time)

        queue.task_done()


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--doctors", type=int, default=NUM_DOCTORS, help="Number of doctors"
    )
    parser.add_argument(
        "--duration",
        type=float,
        default=SHIFT_DURATION,
        help="Shift duration in seconds",
    )
    args = parser.parse_args()

    waiting_room: asyncio.PriorityQueue = asyncio.PriorityQueue()
    stats = {"total_patients": 0, "wait_times": [], "total_times": []}

    shift_end = asyncio.Event()

    # Start doctors
    doctors = [
        asyncio.create_task(doctor(waiting_room, i, stats))
        for i in range(1, args.doctors + 1)
    ]

    # Start arrivals
    door_task = asyncio.create_task(front_door(waiting_room, shift_end))

    await asyncio.sleep(args.duration)
    logging.info("🔒 SHIFT CHANGE - Closing doors...")
    shift_end.set()

    await door_task
    await waiting_room.join()

    # Final stats
    if stats["wait_times"]:
        avg_wait = sum(stats["wait_times"]) / len(stats["wait_times"])
        max_wait = max(stats["wait_times"])
        logging.info(
            f"✅ SIMULATION COMPLETE | {stats['total_patients']} patients treated | Avg wait: {avg_wait:.1f}s | Max wait: {max_wait:.1f}s"
        )

    for d in doctors:
        d.cancel()


async def front_door(queue, shift_end):
    p_id = 1
    while not shift_end.is_set():
        await patient_register(queue, p_id)
        p_id += 1
        await asyncio.sleep(random.uniform(ARRIVAL_SPEED_MIN, ARRIVAL_SPEED_MAX))


if __name__ == "__main__":
    asyncio.run(main())
