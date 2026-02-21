# AI-Agentic Journey: My 18-Month Roadmap to Agentic AI Engineer (2026)

**Made with Gemini's Deep Research**  
**Custom for my HealthTech goals (Project MERITUM)**

**Status:** Month 1 COMPLETE ✅ (Triage Simulation shipped)  
**Next milestone:** Start Month 2 – Structure & Validation (Pydantic)

This is my public 18-month learning journey from Python beginner → production-ready Agentic AI Engineer.  
Everything is built around real 2026 needs: async-first, structured outputs, local-first (Ollama), domain grounding, and rigorous evals.

---

## High-Level Roadmap

### Phase 1: The Modern Foundation (Months 1–3)
**Goal:** Fluency in "AI-Native" Python.  
- Asyncio mastery (agents run in parallel)  
- Pydantic + Type Hinting (force LLMs to output structured data)  
- First LLM primitive (summarize files, structured extraction)

### Phase 2: Orchestration & Data (Months 4–6)
**Goal:** Build the "Brain" and "Memory."  
- LangGraph stateful agents (Research → Critique → Rewrite loops)  
- RAG + Vector DBs (Chat with PDF, advanced chunking)  
- Tool use (SQL, web search)

### Phase 3: The Domain Project (Months 7–12)
**Goal:** Proof of Agency & Domain Moat.  
- Hard domain project (HealthTech focus)  
- Full eval suite with golden answers + LLM-as-judge  
- Guardrails & human-in-the-loop

### Phase 4: Integration & Operations (Months 13–18)
**Goal:** Production Readiness.  
- Docker + cloud deployment  
- Observability (LangSmith/Arize)  
- Open-source contribution (this becomes my resume)

## Conclusion – The Verdict
Coding syntax is becoming obsolete.  
The future belongs to **AI Systems Architects** who design intent, orchestrate agents, and ground them in truth.

**Final Recommendation:**  
Learn Python **for Agentic Orchestration**. Build in public. Ship real domain value.

---

## Table of Contents for Further Study
- **Strategic Concepts:** Agentic Workflows, Knowledge Layer, Sovereign AI Stack  
- **Technical Competencies:** LangGraph, Vector DBs, DSPy, Guardrails  
- **Target Roles:** AI Systems Architect, Bioinformatics/AI in HealthTech

---

## In-Depth Daily Curriculum – Phase 1 Only
*(Phases 2–4 will be expanded here as I progress)*

### Month 1: The Asynchronous Mindset
**Objective:** Shift from sequential to concurrent thinking.  
**Deliverable:** High-throughput Async Scraper + Triage Simulation


| D   | Task / Activity                                                                                                      | Learning Outcome / Insight                                                     | Hs  |
| --- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | --- |
| 1   | Setup & Sync: Install Python 3.11+. Write a script that prints "Hello", sleeps 2s (time.sleep), prints "World".      | Baseline for synchronous (blocking) behavior.                                  | 2   |
| 2   | The Async Keyword: Rewrite Day 1 script using async def and await asyncio.sleep(2). Run with asyncio.run().          | Introduction to non-blocking syntax.                                           | 2   |
| 3   | The Event Loop: Watch "Visualizing the Event Loop".21 Write a script with 3 functions sleeping for different times.  | Understanding the "Scheduler" concept (The Triage Nurse).                      | 3   |
| 4   | Gathering Tasks: Use asyncio.gather() to run the 3 functions from Day 3 simultaneously. Measure execution time.      | Epiphany: Code runs in the time of the slowest task, not the sum of all tasks. | 2   |
| 5   | Background Tasks: Use asyncio.create_task() to run a "heartbeat" (print "beep" every 1s) while a main task waits 5s. | Parallelism concept: Monitoring a patient while filling paperwork.             | 2   |
| 6   | Blocking the Loop: Experiment: Put time.sleep inside an async function. Watch the heartbeat stop.                    | Crucial: Understanding how one blocking action freezes the whole system.       | 3   |
| 7   | Rest & Review: Review the week's code. Read asyncio docs on RealPython.                                              | Consolidation.                                                                 | -   |
| 8   | HTTP Requests: Install httpx. Write a script to fetch https://example.com asynchronously.                            | The Agent's ability to reach the outside world.                                | 2   |
| 9   | Concurrency at Scale: Fetch 50 URLs (use JSONPlaceholder API). Use a for loop (bad) vs gather (good).                | Realizing the speed difference (seconds vs milliseconds).                      | 2   |
| 10  | Semaphores (Rate Limiting): Fetch 100 URLs but limit to 5 at a time using asyncio.Semaphore.                         | Control: Preventing the system from overwhelming external services.            | 3   |
| 11  | Error Handling: Introduce a bad URL. Use try/except inside the tasks. Use return_exceptions=True.                    | Resilience: Ensuring one failure doesn't crash the whole application.          | 2   |
| 12  | Timeouts: Use asyncio.wait_for() to cancel a request if it takes >2s.                                                | Boundaries: Setting strict time limits on interactions.                        | 2   |
| 13  | Context Managers: Use async with httpx.AsyncClient() as client.                                                      | Resource management (opening/closing sessions properly).                       | 3   |
| 14  | Mini-Project: "The Async Scraper." Scrape titles from 20 documentation pages. Save to a file.                        | Portfolio Piece: Demonstrates basic Async mastery.                             | 5   |
| 15  | Socket Programming (Intro): Read about WebSockets vs HTTP.                                                           | Real-time communication theory (Chatbots).                                     | 2   |
| 16  | Simple Chat Server: Use python-socketio or websockets library. Build a basic echo server.                            | Moving from "Request/Response" to "Persistent Connection."                     | 3   |
| 17  | Handling Multiple Clients: Connect 2 terminal windows to the chat server. Chat between them.                         | Managing multi-user state.                                                     | 3   |
| 18  | Async Queues: Use asyncio.Queue. Producer (Client) -> Queue -> Consumer (Server).                                    | Buffering inputs (Triage queue).                                               | 2   |
| 19  | Refactoring: Clean up the Chat Server code. Add type hints (generic).                                                | Preparing for strict typing.                                                   | 2   |
| 20  | Review: Re-read code. Annotate "what is blocking" and "what is awaiting".                                            | Deepening the mental model.                                                    | 3   |
| 21  | Rest & Review                                                                                                        |                                                                                | -   |
| 22  | Project Planning: Design "The Triage Simulation." 100 patients arrive randomly. 3 doctors process them.              | Design Phase: Mapping the architecture before coding.                          | 3   |
| 23  | Coding Triage: Implement the "Patient" class and "Doctor" coroutine.                                                 | Application of Object-Oriented Async.                                          | 3   |
| 24  | Coding Triage: Implement the Queue and Arrival logic.                                                                | Flow control.                                                                  | 3   |
| 25  | Coding Triage: Add logging. Print when a patient starts/finishes.                                                    | Observability.                                                                 | 2   |
| 26  | Optimization: Tweak the number of doctors. See how wait times change.                                                | Systems Thinking: Balancing load and resources.                                | 3   |
| 27  | Final Polish: Add a "Shift Change" event that stops new arrivals.                                                    | Graceful shutdown patterns.                                                    | 3   |
| 28  | Documentation: Write a README explaining the logic.                                                                  | Communication skills.                                                          | 2   |
| 29  | Capstone Review: Post code to GitHub.                                                                                | Public accountability.                                                         | 2   |
| 30  | Rest & Reflection                                                                                                    |                                                                                | -   |

### Month 2: Structure & Validation (Pydantic v2)
**Objective:** Force chaos into structure.  
**Deliverable:** Medical Intake Validator CLI

|     |                                                                                                       |                                                         |     |
| --- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | --- |
| D   | Task / Activity                                                                                       | Learning Outcome / Insight                              | H   |
| 31  | Type Hinting: Read Python typing docs (List, Dict, Optional, Union).                                  | Precision in language.                                  | 2   |
| 32  | Pydantic Basics: Install pydantic. Create a User model. Validate a dict.                              | The "Intake Form" concept.                              | 2   |
| 33  | Strict Types: Try passing a string to an int field. Watch Pydantic coerce or fail.                    | Data integrity enforcement.                             | 2   |
| 34  | Field Metadata: Use Field(..., description="...").                                                    | Documenting the schema for the AI (later use).          | 2   |
| 35  | Validation Logic: Use @field_validator. Ensure age > 0.                                               | Clinical Logic: Implementing "Reality Testing" in code. | 3   |
| 36  | Complex Validation: Validator that checks 2 fields (e.g., if under_18, ensure parent_contact exists). | Contextual Logic: Dependencies between data points.     | 3   |
| 37  | Nested Models: Create Address model, put it inside User.                                              | Handling hierarchical data (Case History).              | 2   |
| 38  | Serialization: model.model_dump() and model_dump_json().                                              | Preparing data for API transmission.                    | 2   |
| 39  | Custom Types: Use EmailStr, HttpUrl from Pydantic.                                                    | Leveraging built-in validation tools.                   | 2   |
| 40  | Settings Management: Use pydantic-settings to read .env files.                                        | Security: Handling API keys safely.                     | 3   |
| 41  | Review & Rest                                                                                         |                                                         | -   |
| 42  | JSON Parsing: Read a complex JSON file into a Pydantic model.                                         | Ingesting external data.                                | 3   |
| 43  | Error Handling: Catch ValidationError. Print readable error messages for users.                       | UX: Translating technical errors into human guidance.   | 3   |
| 44  | Discriminated Unions: Handle different types of events (Message, Image, SystemLog) in one list.       | Polymorphism (handling diverse inputs).                 | 4   |
| 45  | Generic Models: Create a Response wrapper model.                                                      | Advanced abstraction.                                   | 3   |
| 46  | Computed Fields: @computed_field. Calculate bmi from height and weight automatically.                 | Automating derived data.                                | 2   |
| 47  | Immutability: ConfigDict(frozen=True).                                                                | Creating "Read-Only" records (Clinical integrity).      | 2   |
| 48  | Rest & Review                                                                                         |                                                         | -   |
| 49  | Project Planning: "The Intake Validator." CLI tool for medical data entry.                            | Design phase.                                           | 2   |
| 50  | Implementation: Define models (Patient, Symptom, History).                                            | Schema design.                                          | 3   |
| 51  | Implementation: Write the input() loop to ask users for data.                                         | Interactive scripting.                                  | 3   |
| 52  | Implementation: Validate inputs. Retry on error ("Invalid age, try again").                           | The Loop: Interactive validation cycles.                | 3   |
| 53  | Implementation: Save valid records to a JSON file.                                                    | Persistence.                                            | 2   |
| 54  | Testing: Write pytest tests for your models.                                                          | Quality Assurance: Ensuring the validators work.        | 4   |
| 55  | Refinement: Add a "Summary" feature that prints a formatted report.                                   | Data presentation.                                      | 2   |
| 56  | Integration: Combine with Month 1 concepts (Async file writing).                                      | Synthesizing skills.                                    | 3   |
| 57  | Documentation: Document the Schema.                                                                   | Clarity.                                                | 2   |
| 58  | Capstone Review: Publish to GitHub.                                                                   | Portfolio building.                                     | 2   |
| 59  | Deep Read: Read "Parse, Don't Validate" blog post (conceptual).                                       | Philosophy of Type-Driven Design.                       | 2   |
| 60  | Rest & Reflection                                                                                     |                                                         | -   |

### Month 3: The Primitive (LLM APIs & Agents)
**Objective:** Connect Async + Pydantic + LLM.  
**Deliverable:** Therapeutic Copilot (with Ollama + OpenAI switch)

|   |   |   |   |
|---|---|---|---|
|D|Task / Activity|Learning Outcome / Insight|H|
|61|API Access: Get OpenAI Key. Install openai lib. Send "Hello".|First contact.|2|
|62|Async Client: Use AsyncOpenAI. Await the response.|Non-blocking intelligence.|2|
|63|System Prompts: Define a "Persona". Change the behavior via prompt.|Therapeutic Frame: Setting the context.|2|
|64|Streaming: Use .stream(). Print tokens as they arrive.|UX: Reducing perceived latency.|3|
|65|Structured Output (Intro): Prompt: "Return JSON only." See it fail/succeed.|The difficulty of non-deterministic output.|2|
|66|Instructor Library: Install instructor. Patch the client.|The Magic: Forcing Pydantic models on LLMs.|3|
|67|Extraction: Feed a bio text. Extract User model using Instructor.|converting text to data.|3|
|68|Validation & Retries: Feed bad data. Watch Instructor retry automatically.|Self-Correction: The system healing itself.|3|
|69|Rest & Review||-|
|70|Tools (Function Calling): Define a calculate_bmi function. Give it to LLM.|Giving the AI "Hands."|3|
|71|Tool Execution: Parse the tool call, run the Python function, return result.|The Agent Loop: Thought -> Action -> Observation.|4|
|72|Chat History: Maintain a list of messages. Append user/assistant turns.|State: Memory management.|3|
|73|Context Window: What happens when history is too long? (Truncation).|Resource management.|2|
|74|RAG (Basic): Search a text file for a keyword, inject into prompt.|Grounding: Providing facts to the AI.|4|
|75|Agent Loop: Build a while True loop that allows tool use.|The "Godot" loop applied to AI.|4|
|76|Rest & Review||-|
|77|Capstone Planning: "The Therapeutic Copilot." A bot that helps format session notes.|Domain application.|3|
|78|Architecture: User Input -> Async Queue -> Agent -> Pydantic Validation -> Output.|System Design.|3|
|79|Model Design: Define SessionNote model (Subjective, Objective, Plan).|Schema definition.|2|
|80|Agent Logic: Prompt engineering for summarizing therapy transcripts.|Domain expertise application.|3|
|81|Implementation: Build the core processing loop.|Coding.|4|
|82|Guardrails: Add a check for "Self Harm" markers.|Safety: Human-in-the-Loop design.|4|
|83|UI (Terminal): Make it look nice with rich library.|Usability.|2|
|84|Testing: Run with fake transcripts. Tune the prompt.|Iterative improvement.|3|
|85|Refactoring: Clean code, add types, add comments.|Professional polish.|3|
|86|Deployment (Simulated): Run in a Docker container (intro to Docker).|portability.|4|
|87|Documentation: Write a case study on the GitHub repo.|Marketing: Selling the skill.|3|
|88|Portfolio Review: Polish all 3 month's repos.|Finalizing the package.|4|
|89|Community: Join a Discord/Slack and share the project.|Networking.|2|
|90|Rest & Celebration|Phase 1 Complete.|-|

**Last updated:** February 18, 2026  
**Built for 2026 reality** — Async-first, local-first (Ollama), production mindset.