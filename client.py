import asyncio
import socket
import logging
import sys
from tkinter import messagebox

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)


class Client(object):

    def __init__(self):
        # インスタンス作成と同時にクライアント側のソケット作成
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client.setblocking(False)

    async def connect(self, host, port):
        loop = asyncio.get_event_loop()
        await loop.sock_connect(host, port)

    async def auto_send_checkbox(self):
        pass

    async def send(self, msg):
        loop = asyncio.get_event_loop()
        await loop.sock_sendall(self.client, msg)

    def send_b(self):
        pass

    def clear(self):
        """
        クリアボタン押されたら、ファイルの中身を初期化
        :return:
        """
        with open('b.csv', 'wb') as f:
            f.truncate(0)

    def close(self):
        self.client.close()
