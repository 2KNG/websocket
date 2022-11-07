import asyncio
import websockets


class EtomServer:
    def __init__(self):
        self.clients = []
        self.data = 0
    async def echo(self, websocket):
        self.clients.append(websocket)
        await websocket.send("Welcome to ETOM")
        async for message in websocket:
            for client in self.clients:
                await client.send(message)
            # websocket.broadcast(self.clients, message)


# async def handler(websocket):
#     connected = {websocket}
#
# async def echo(websocket):
#     await websocket.send("connected")
#     async for message in websocket:
#         websockets.broadcast()
#         await websocket.send(message)
#
# async def accept(websocket):
#     await websocket.send("Welcome to ETOM")
#     while True:
#         global data
#         data = await websocket.recv()
#         if data:
#             await websocket.send(data)
#             print(data)
etom = EtomServer()
start_server = websockets.serve(etom.echo, "0.0.0.0", 7712)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()