import socket
import json
from threading import Thread


#服务器信息
host = "127.0.0.1"
port = 50008
#连接对象池
conns = []


def deply(conn):
    global conns
    print(conns)
    while True:#合法：把消息打包传送给其他连接对象
        try:
            data = conn.recv(1024).decode()
        except Exception as e:
            print(e)
            conns.remove(conn)
            break
        data = json.loads(data)
        if 'user' in data.key and 'content' in data.keys():
            for c in conns: #拿出一个c就是连接对象
                c.sendall(json.dumps(data).encode())

            if data['content'] == 'bye':#退出
                conns.remove(conn)
                break

    conn.close()#当前连接关闭

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind((host,port))
s.listen(200)
print("Chat server started")
while True:
    conn,addr = s.accept()
    print(f"一位新用户连接到服务器，地址是{addr}")
    print(conn)
    conn.append(conn)
    Thread(target=deply,args=(conn,)).start()
