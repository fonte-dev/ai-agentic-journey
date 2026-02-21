# 🏥 Async Triage Simulation

An asynchronous hospital emergency room simulator built in Python to demonstrate concurrent processing, object-oriented asynchronous design, and system flow control.

## 📌 Overview
This simulation uses Python's `asyncio` library to model a hospital triage system. 
- **Producers (Patients):** Arrive at random intervals with varying severity levels (1-Critical to 5-Minor).
- **State (Waiting Room):** An `asyncio.PriorityQueue` automatically sorts incoming patients so doctors always treat the most critical patients first.
- **Consumers (Doctors):** Asynchronous worker tasks that pull patients from the queue and simulate treatment times based on severity.
- **Graceful Shutdown:** The simulation runs for a set shift duration, locks the doors to new arrivals, and allows doctors to finish treating the remaining backlog before shutting down safely.

## ⚙️ Requirements
- Python 3.11+
- [Faker](https://faker.readthedocs.io/) (for generating realistic patient names)

**Installation:**
```bash
pip install faker
```

## 🚀 How to Run
Run the simulation directly from your terminal:
```bash
python triage_simulation.py
```

## 🛠️ Configuration
You can test the system's performance under stress by tweaking the global parameters at the top of `triage_simulation.py`:
- `SHIFT_DURATION = 15.0`: How long (in seconds) the hospital doors remain open.
- `NUM_DOCTORS = 3`: The number of concurrent doctor tasks running.
- `ARRIVAL_SPEED_MIN = 1.0` / `ARRIVAL_SPEED_MAX = 3.0`: The random time interval between patient arrivals.

Try lowering the arrival speed to 0.1 and setting `NUM_DOCTORS` to 1 to watch the backlog explode!

## Why this project matters for my journey
This simulation is the perfect technical foundation for **MERITUM** — my meritocratic platform for Acompañantes Terapéuticos. 
It proves I can build concurrent, resilient, observable systems that deal with real-world priorities (critical patients = critical cases in mental health).

Next stop: Month 2 (Pydantic mastery) → then the Therapeutic Copilot.