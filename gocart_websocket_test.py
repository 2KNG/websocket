import asyncio
import websockets
import threading

robot_message = 0

ip = "0.0.0.0"
# ip = "etom.run"

def ws_thread():
    async def connect():
        # 웹 소켓에 접속을 합니다.
        async with websockets.connect("ws://{}:7712".format(ip), ping_interval=None) as websocket:
            await websocket.send("mac connected")
            while True:
                data = await websocket.recv()
                print(data)
                # if robot_message:
                #     robot_message = 0
                # print("test")

    asyncio.run(connect())

ws_thread()

#
# ws_connect = threading.Thread(target=ws_thread, daemon=False)
# ws_connect.start()