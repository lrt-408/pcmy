import socket
import json
from threading import Thread

#服务器信息
host = "127.0.0.1"
port = 50008
#连接对象池
conns = []

#一个客户端对应一个进程
def deply(conn):
    global conns
    print(conns)
    while True:
        #防止内存溢出
        try:
            data = conn.recv(1024).decode()
        except Exception as e:
            print(e)
            conns.remove(conn)
            break
        #json.load将接送字符数据转换为字典
        data = json.loads(data)
        print(data)
        if 'user' in data.keys() and 'content' in data.keys():
            for c in conns:
                c.sendall(json.dumps(data).encode())
            #内容传送结束后，删掉对象
            if data['content'] == 'bye':
                conns.remove(conn)
                break
    #断开连接
    conn.close()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
#同时监听200个线程
s.listen(200)
print("Chat serve start!")

while True:
    conn,addr = s.accept()
    print(f"一位新用户连接到服务器，地址是{addr}")
    print(conn)
    conns.append(conn)
    Thread(target=deply,args=(conn,)).start()


