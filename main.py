# from server.socket_ser import Server
# main 구동
# from server import socket_cli
from src.game import Game
import time

if __name__ == '__main__':
    # socket_cli
    ga = Game()
    while True:
        if ga.controlData != "":
            print(ga.controlData)
            time.sleep(0.1)


