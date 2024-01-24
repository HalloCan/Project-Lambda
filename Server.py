'''
Project Lambda Version Alpha 0.1
Credit HalloCandy 2024
Build Time: Jan 24 2024 19:57
'''
import socket
import threading

# 创建一个 socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名，默认监听Localhost
host = socket.gethostname ()
serverip = 'localhost'
port = 61122  # 设置端口号

# 绑定端口号
server_socket.bind((host, port))

# 设置最大连接数，超过后排队
server_socket.listen(5)

print(f"服务器启动，监听来自 {host} 的连接，端口号为 {port}")

# 存储所有连接的客户端
clients = []

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

# 广播消息给所有客户端
def broadcast(message, sender_socket):
    for client, _ in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                # 客户端连接出现问题时移除
                clients.remove((client, _))

# 循环等待客户端的连接
while True:
    # 阻塞等待客户端连接
    client_socket, addr = server_socket.accept()
    print(f"建立连接，来自: {addr}")

    # 将新连接的客户端加入列表
    clients.append((client_socket, addr))

    # 创建一个新的线程来处理客户端连接
    client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_handler.start()