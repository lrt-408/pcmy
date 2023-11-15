import socket
import json
from threading import Thread


#服务器信息
host = "127.0.0.1"#10.126.47.105
port = 50008

#专门一个线程用来接收消息
def recv_data(conn):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            continue
        data = json.loads(data)#字符串转换成字典:解包
        user = data['user']
        content = data ['content']
        print(f"【{user}】:{content}")


#主线程发送数据
conn = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
conn.connect((host,port))#生成长连接

Thread(target=recv_data,args = (conn,)).start()
user = input("请输入你的ID:")
print("输入内容开始聊天：")
while True:
    input_data = input()
    data = {
        'user':user,
        'content': input_data,
    }
    conn.sendall(json.dumps(data).encode())
    if input_data == 'bye':
        break

conn.close()