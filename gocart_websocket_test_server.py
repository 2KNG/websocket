import asyncio
import websockets


async def accept(websocket):
    while True:
        data = await websocket.recv()
        if data:
            await websocket.send(data)
            data = 0


start_server = websockets.serve(accept, "localhost", 7712)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()