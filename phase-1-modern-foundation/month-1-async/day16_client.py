# Day 16 - Simple Chat (Client)
# Task: Simple Chat Server: Use python-socketio or websockets library. Build a basic echo server.
# Learning goal: Moving from "Request/Response" to "Persistent Connection."
# Date: Feb 2026
# Status: Done ✅

import asyncio
import websockets


async def chat():
    # Notice the protocol is 'ws://' not 'http://'
    uri = "ws://localhost:8765"

    print(f"Connecting to {uri}...")

    # Open the persistent connection
    async with websockets.connect(uri) as websocket:
        print("🟢 Connected! Type 'quit' to exit.")

        while True:
            # 1. Get input from the user (This is blocking, but okay for a simple client)
            msg = input("\nYou: ").strip()

            if msg.lower() == "quit":
                print("Disconnecting...")
                break

            # 2. Push the message through the open pipe
            await websocket.send(msg)

            # 3. Wait for the server to push something back
            response = await websocket.recv()
            print(f"Server: {response}")


if __name__ == "__main__":
    try:
        asyncio.run(chat())
    except KeyboardInterrupt:
        print("\nExited.")
