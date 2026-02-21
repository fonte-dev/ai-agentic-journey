# Day 17 - Multiple Clients Chat (Server)
# Task: Handling Multiple Clients: Connect 2 terminal windows to the chat server. Chat between them.
# Learning goal: Managing multi-user state.
# Date: Feb 2026
# Status: Done ✅

import asyncio
import websockets

# THIS IS THE STATE: A memory of all people in the room.
# We use a set() because it automatically handles unique items (no duplicates).
connected_clients = set()


async def chat_handler(websocket):
    # 1. Register the new client
    connected_clients.add(websocket)
    print(f"New client joined! Total in room: {len(connected_clients)}")

    try:
        # 2. Listen for their messages
        async for message in websocket:
            print(f"Received: {message}")

            # 3. Broadcast to EVERYONE (including the sender)
            # websockets.broadcast is a built-in helper that sends a message
            # to a whole list/set of connections simultaneously.
            websockets.broadcast(connected_clients, message)

    except websockets.exceptions.ConnectionClosed:
        pass  # We handle cleanup in the 'finally' block

    finally:
        # 4. Unregister the client when they leave
        # This is critical. If we don't remove them, the server will
        # try to send messages to a dead connection and crash.
        connected_clients.remove(websocket)
        print(f"Client left. Total in room: {len(connected_clients)}")


async def main():
    print("Chat Room Server running on ws://localhost:8765")
    async with websockets.serve(chat_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
