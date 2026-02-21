# Day 16 - Simple Chat (Server)
# Task: Simple Chat Server: Use python-socketio or websockets library. Build a basic echo server.
# Learning goal: Moving from "Request/Response" to "Persistent Connection."
# Date: Feb 2026
# Status: Done ✅

import asyncio
import websockets


async def echo_handler(websocket):
    # This function runs whenever a new client connects.
    print("🟢 New client connected!")

    try:
        # This is an asynchronous infinite loop!
        # It pauses here until a message arrives. It does NOT block other code.
        async for message in websocket:
            print(f"Received from client: {message}")

            # Simulate the AI "thinking"
            await asyncio.sleep(0.5)

            # Send it right back
            reply = f"Echo: {message}"
            print(f"Sending back: {reply}")
            await websocket.send(reply)

    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected cleanly.")
    except Exception as e:
        print(f"Error: {e}")


async def main():
    # Start the server on port 8765
    print("WebSocket Echo Server starting on ws://localhost:8765")

    # async with ensures the server shuts down gracefully if we crash
    async with websockets.serve(echo_handler, "localhost", 8765):
        # This tells the server to run forever until we press Ctrl+C
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
