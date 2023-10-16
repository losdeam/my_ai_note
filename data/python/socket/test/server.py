'''
遇到问题没人解答？小编创建了一个Python学习交流QQ群：857662006 
寻找有志同道合的小伙伴，互帮互助,群里还有不错的视频学习教程和PDF电子书！
'''
import socket
from time import ctime
import json
import time
HOST = ''
PORT = 9001
ADDR = (HOST, PORT)
BUFFSIZE = 1024
MAX_LISTEN = 5


def tcpServer():
    # TCP服务
    # with socket.socket() as s:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 绑定服务器地址和端口
        s.bind(ADDR)
        # 启动服务监听
        s.listen(MAX_LISTEN)
        print('等待用户接入。。。。。。。。。。。。')
        while True:
            # 等待客户端连接请求,获取connSock
            conn, addr = s.accept()
            print('警告，远端客户:{} 接入系统！！！'.format(addr))
            with conn:
                while True:
                    print('接收请求信息。。。。。')
                    # 接收请求信息
                    data = conn.recv(BUFFSIZE)
                    print('data=%s' % data)
                    print('接收数据：{!r}'.format(data.decode('utf-8')))
                    if data == "quit":
                        break
                    # 发送请求数据
                    conn.send(data.encode('utf-8'))
                    print('发送返回完毕！！！')
            s.close()


# 创建UDP服务
def udpServer():
    # 创建UPD服务端套接字
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # 绑定地址和端口
        s.bind(ADDR)
        # 等待接收信息
        while True:
            print('UDP服务启动，准备接收数据。。。')
            # 接收数据和客户端请求地址
            data, address = s.recvfrom(BUFFSIZE)
            if not data:
                break
            data = data.decode('utf-8')
            print('接收请求信息：{}'.format(data))
            print(address)
            if data == "quit":
                break
            s.sendto(b'i am udp,i got it', address)

        s.close()

if __name__ == '__main__':

    while True:
        choice = input('input choice t-tcp or u-udp or q-quit:')

        if choice == 't':
            print('execute tcpsever')
            tcpServer()

        elif choice == 'u':
            print('execute udpsever')
            udpServer()
        elif choice == 'q':
            break
        else :
            print('please input t or u,ok?')
            continue