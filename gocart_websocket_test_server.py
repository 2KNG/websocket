import asyncio
import websockets


async def accept(websocket):
    while True:
        data = await websocket.recv()
        if data:
            await websocket.send(data)
            print(data)
            data = 0


start_server = websockets.serve(accept, "0.0.0.0", 7712)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()