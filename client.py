import socket
import logging

logger = logging.getLogger(__name__)


class Client(object):
    def __init__(self, ip='192.168.8.225', port='8888'):
        self.ip = ip
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip, self.port))

    def connect(self, ip, port):
        try:
            self.socket.connect((ip, port))
        except socket.error as ex:
            logger.info({'action': 'connect', 'ip': ip, 'port': port, 'ex': ex})

    def close(self):
        self.socket.close()
