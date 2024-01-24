def serverinfo():
    while True:
            host = input("请输入远程主机地址：")
            port = input("请输入远程主机端口：")
            if host == '' or port == '' or int(port) > 65535 or int(port) < 0:
                print("服务器信息有误！")
            else:
                break
    return host, port
print(serverinfo())