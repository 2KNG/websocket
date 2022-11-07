import asyncio
import websockets

data = 0

async def accept(websocket):
    await websocket.send("Welcome to ETOM")
    while True:
        global data
        data = await websocket.recv()
        if data:
            await websocket.send(data)
            print(data)

start_server = websockets.serve(accept, "0.0.0.0", 7712)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()