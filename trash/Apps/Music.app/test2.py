import asyncio
from websockets import serve

async def echo(websocket):
    try:
        async for message in websocket:
            print("received",len(message))
    except:
        pass

async def main():
    async with serve(echo, "localhost", 42069):
        await asyncio.Future()  # run forever

asyncio.run(main())