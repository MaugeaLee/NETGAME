import socket
from config import constant


"""
서버 개시 클래스
"""
class Server():
    def __init__(self):
        # init
        self.HOST = constant.HOST
        self.PORT = constant.PORT
        self.LISTEN = constant.SERVER_LISTEN

        self.server_socket = ""
        self.accept_socket = ""
        self.client_address = ""

        self.serverInit()

    def serverInit(self):
        # server_socket init
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind( (self.HOST, self.PORT))
        self.server_socket.listen(self.LISTEN)
        print("server open HOST : {} \nserver open PORT : {}".format(self.HOST, self.PORT))

        # server accept
        try:
            print("server accept load ...")
            self.accept_socket, self.client_address = self.server_socket.accept()
            print(str(self.client_address), 'connect accept')

        except KeyboardInterrupt as e:
            print("서버 중지")

        finally:
            self.server_socket.close()
            if self.accept_socket != "":
                print(self.accept_socket)
                self.accept_socket.close()

    def comunication(self):
        pass