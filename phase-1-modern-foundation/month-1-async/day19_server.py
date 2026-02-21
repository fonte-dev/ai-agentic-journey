# Day 19 - Type Hints
# Task: Refactoring: Clean up the Chat Server code. Add type hints (generic).
# Learning goal: Preparing for strict typing.
# Date: Feb 2026
# Status: Done ✅

import asyncio
import websockets

# We import the specific network "Type" (ServerConnection) from the asyncio module
from websockets.asyncio.server import ServerConnection

# 1. State Type Hinting
# We explicitly tell Python: "This is a set that ONLY contains ServerConnection objects."
connected_clients: set[ServerConnection] = set()


# 2. Function Argument and Return Type Hinting
# websocket MUST be a ServerConnection object. The function returns nothing (-> None).
async def chat_handler(websocket: ServerConnection) -> None:
    websocket.send
    connected_clients.add(websocket)
    print(f"New client joined! Total in room: {len(connected_clients)}")

    try:
        async for message in websocket:
            # 3. Local Variable Type Hinting
            # We enforce that the incoming message is treated as a string
            msg: str = str(message)
            print(f"Received: {msg}")

            websockets.broadcast(connected_clients, msg)

    except websockets.exceptions.ConnectionClosed:
        pass

    finally:
        connected_clients.remove(websocket)
        print(f"Client left. Total in room: {len(connected_clients)}")


# 4. Main returns nothing
async def main() -> None:
    print("Strictly Typed Chat Server running on ws://localhost:8765")
    async with websockets.serve(chat_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
