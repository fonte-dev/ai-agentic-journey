# Day 17 - Multiple Clients Chat (Client)
# Task: Handling Multiple Clients: Connect 2 terminal windows to the chat server. Chat between them.
# Learning goal: Managing multi-user state.
# Date: Feb 2026
# Status: Done ✅

import asyncio
import websockets


async def receive_messages(websocket):
    """Task 1: Constantly listen for messages from the server."""
    try:
        async for message in websocket:
            print(f"\n{message}")
    except websockets.exceptions.ConnectionClosed:
        print("\nServer closed the connection.")


async def send_messages(websocket, username):
    """Task 2: Wait for user input and send it."""
    while True:
        # asyncio.to_thread runs the blocking input() function in the background
        # so it doesn't freeze our listening task!
        msg = await asyncio.to_thread(input, "")

        if msg.lower() == "quit":
            break

        formatted_msg = f"[{username}]: {msg}"
        await websocket.send(formatted_msg)


async def main():
    uri = "ws://localhost:8765"
    username = input("Enter your username: ").strip()

    async with websockets.connect(uri) as websocket:
        print(f"Connected to the room as {username}! (Type 'quit' to exit)")

        # Announce arrival
        await websocket.send(f"👋 {username} has joined the room!")

        # Start both tasks simultaneously
        listen_task = asyncio.create_task(receive_messages(websocket))
        talk_task = asyncio.create_task(send_messages(websocket, username))

        # Wait until the user types 'quit' (which stops talk_task)
        await talk_task
        listen_task.cancel()  # Stop listening when we quit


if __name__ == "__main__":
    asyncio.run(main())
