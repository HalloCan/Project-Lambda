'''
Project Lambda Version Alpha 0.1
Credit HalloCandy 2024
Build Time: Jan 24 2024 19:57
'''
import socket
import threading

# 创建一个 socket 对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取远程主机名
host = 'localhost'
port = 61122  # 设置端口号

# 连接服务，指定主机和端口
client_socket.connect((host, port))

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

# 发送消息给服务器
while True:
    message = input("请输入消息: ")
    client_socket.send(message.encode('utf-8'))

# 关闭连接
client_socket.close()