'''
Project Lambda Version Alpha 0.1.3
Credit HalloCandy 2024
Build Time: Jan 24 2024 23:14
'''
from sys import exit as sexit
import socket
import threading

# 创建一个 socket 对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取远程主机名
def serverinfo():
    while True:
            host = input("请输入远程主机地址：")
            port = input("请输入远程主机端口：")
            if host == '' or port == '' or int(port) > 65535 or int(port) < 0:
                print("服务器信息有误！")
            else:
                break
    return host, port


host, port = serverinfo()


# 连接服务，指定主机和端口
client_socket.connect((host, int(port)))

# 接收服务器消息的线程
def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            print(f"接收到服务器的消息: {data.decode('utf-8')}")
        except:
            break

# 启动接收消息的线程
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()
print("请输入消息，输入#STOP退出连接并关闭:")
# 发送消息给服务器
while True:
    message = input()
    if message == "#STOP":
        client_socket.close()   # 关闭连接
        sexit()
    else:
        client_socket.send(message.encode('utf-8'))

