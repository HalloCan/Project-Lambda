'''
Project Lambda Version Alpha 0.1.3
Credit HalloCandy 2024
Build Time: Jan 24 2024 23:14
'''
from sys import exit as sexit
import socket
import threading

# 处理服务器ip和端口
def net():
    legacy_IP = socket.gethostbyname(socket.gethostname())
    ipif = input(f'自动获取的服务器ip为{legacy_IP},请输入服务器外网IP,无误请忽略')
    if ipif == '':
        realip = legacy_IP
    else:
        realip = ipif
    portif = input('默认端口为61122,请输入端口号,无误请忽略')
    if portif == '':
        realport = 61122
    else:
        realport = int(portif)

    return realip,realport

# 处理连接的客户端
def handle_client(client_socket, client_address):
    while True:
        # 接收客户端发送的数据
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode('utf-8')
        print(f"接收到来自 {client_address} 的消息: {message}")

        # 广播消息给其他客户端
        broadcast(message, client_socket)

    # 客户端断开连接时移除
    clients.remove((client_socket, client_address))
    client_socket.close()

# 服务器状态线程
def status():
    print('''1:Server IP
2:Connection String
3:Stop''')
    while True:
        x = input('#?')
        subject = x
        match subject:
            case '1':
                print("1")
            case '2':
                print("2")
            case '3':
                print("现在可以关闭窗口了")
                sexit()
            case _:
                print("NO")

# 广播消息给所有客户端
def broadcast(message, sender_socket):
    for client, _ in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                # 客户端连接出现问题时移除
                clients.remove((client, _))



# 创建一个 socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名，默认监听Localhost
host = socket.gethostname ()
serverip = 'localhost'
realip, port = net()  # 设置端口号

# 绑定端口号
server_socket.bind((serverip, port))

# 设置最大连接数，超过后排队
server_socket.listen(5)

print(f"服务器启动，监听来自 {host} 的连接，端口号为 {port}")

# 存储所有连接的客户端
clients = []

# 创建一个新的线程来处理服务器信息
server_status = threading.Thread(target=status)
server_status.start()

# 循环等待客户端的连接
while True:
    # 阻塞等待客户端连接
    client_socket, addr = server_socket.accept()
    print(f"建立连接，来自: {addr}")
    print('#?')

    # 将新连接的客户端加入列表
    clients.append((client_socket, addr))

    # 创建一个新的线程来处理客户端连接
    client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_handler.start()


