import socket
import json
from threading import Thread

#服务器信息
host = "127.0.0.1"
port = 50008

#用来接收消息的线程
def recv_data(conn):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            #没有数据退出本次循环，开始下一次循环
            continue
        data = json.loads(data)
        user = data['user']
        content = data['content']
        print(f"{user}:{content}")

conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.connect((host,port))
Thread(target=recv_data,args=(conn,)).start()
user = input("请输入你的聊天id:")
print("输入内容开始聊天：")
while True:
    input_data = input()
    data = {
        'user' : user,
        'content' : input_data,
    }
    conn.sendall(json.dumps(data).encode())
    if input_data == "bye":
        break
conn.close()
