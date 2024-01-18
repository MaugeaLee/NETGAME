from config import constant
import socket


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((constant.SERVER_HOST, constant.PORT))
print('서버와 연결이 됐습니다.')

while True:
    # recv_msg = my_socket.recv(1024).decode('utf-8')
    # print('[받은 메시지]', recv_msg)

    send_msg = input('[보낼 메시지]')
    my_socket.send(send_msg.encode('utf-8'))

my_socket.close()