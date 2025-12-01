import tornado.ioloop
import tornado.websocket

class WebSocketClient:
    def __init__(self, io_loop):
        self.connection = None
        self.io_loop = io_loop

    def start(self):
        self.io_loop.add_callback(self.connect_and_read)

    def stop(self):
        self.io_loop.stop()

    async def connect_and_read(self):
        print("Connecting ...")
        try:
            self.connection = await tornado.websocket.websocket_connect(
                url="ws://localhost:8888/websocket/",
                ping_interval=10,
                ping_timeout=30
            )
            print("Connected! Reading messages ...")
            await self.read_message()
        except Exception as e:
            print(f"Could not connect, retrying in 3 seconds ... ({e})")
            self.io_loop.call_later(3, lambda: self.io_loop.add_callback(self.connect_and_read))

    async def read_message(self):
        while True:
            try:
                message = await self.connection.read_message()
                if message is None:
                    print("Disconnected, reconnecting ...")
                    await self.connect_and_read()
                    break
                print(f"Received word from server: {message}")
            except Exception as e:
                print(f"Error: {e}")
                await self.connect_and_read()
                break

def main():
    io_loop = tornado.ioloop.IOLoop.current()
    client = WebSocketClient(io_loop)
    io_loop.add_callback(client.start)
    io_loop.start()

if __name__ == "__main__":
    main()