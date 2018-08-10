# from socket import *

# host='127.0.0.1'
# PORT = 5555
# addr = (host,PORT)
# udpClient = socket(AF_INET, SOCK_DGRAM)
# # udpClient.bind(('0.0.0.0', PORT))

# udpClient.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
# for i in range(100):
#     data = b'hello'
#     if not data:
#         break
#     print('sending -> %s' % data)
#     udpClient.sendto(data,addr)

# import socket

# # 获取本机计算机名称
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# s.connect(("1.1.1.1",80))

# ipaddr=s.getsockname()[0]

# s.close()

# print(ipaddr)

from flask import Flask
from flask_script import Manager
import socket

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def findme():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1",80))
    ipaddr=s.getsockname()[0]
    s.close()

    print(ipaddr)
    return ipaddr


if __name__ =="__main__":
    manager.run()
    

