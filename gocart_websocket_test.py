import asyncio
import websockets
import threading

# HOST = '175.126.123.199'  # Cafe24 ubuntu2
HOST = 'etom.run'  # Cafe24 ubuntu2
PORT = 8180

robot_message = 0

# URL = f'http://{HOST}:{PORT}/wsrobot'


def ws_thread():
    async def connect():
        # 웹 소켓에 접속을 합니다.
        async with websockets.connect("ws://etom.run:7712") as websocket:
            while True:
                await websocket.send("send")
                data = await websocket.recv()
                print(data)
                # if robot_message:
                #     robot_message = 0
                # print("test")

    asyncio.run(connect())
    # asyncio.get_event_loop().run_until_complete(connect())


ws_connect = threading.Thread(target=ws_thread, daemon=True)
ws_connect.start()