'''
遇到问题没人解答？小编创建了一个Python学习交流QQ群：857662006 
寻找有志同道合的小伙伴，互帮互助,群里还有不错的视频学习教程和PDF电子书！
'''
import socket

from time import ctime
HOST = 'localhost'
PORT = 9001
ADDR = (HOST, PORT)
ENCODING = 'utf-8'
BUFFSIZE = 1024


def tcpClient():
    # 创建客户套接字
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        # 尝试连接服务器
        s.connect(ADDR)
        print('连接服务成功！！')
        # 通信循环
        while True:
            inData = input('pleace input something:')
            if inData == 'q':
                break
            # 发送数据到服务器
            inData = '[{}]:{}'.format(ctime(), inData)

            s.send(inData.encode(ENCODING))
            print('发送成功！')

            # 接收返回数据
            outData = s.recv(BUFFSIZE)
            print('返回数据信息：{!r}'.format(outData))

        # 关闭客户端套接字
        s.close()


def udpClient():
    # 创建客户端套接字
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            # 发送信息到服务器
            data = input('please input message to server or input \'quit\':')
            print(data)
            
            s.sendto(data.encode('utf-8'), ADDR)

            print('send success')
            if data == 'quit':
                break
            
            # 接收服务端返回信息
            recvData, addrs = s.recvfrom(BUFFSIZE)
            
            print('recv message : {}'.format(recvData.decode('utf-8')))
            
        # 关闭套接字
        print("已关闭连接")
        s.close()


if __name__ == '__main__':

    while True:
        choice = input('input choice t-tcp or u-udp or q-quit:')
        if choice == 'q':
            break
        elif choice != 't' and choice != 'u':
            print('please input t or u,ok?')
            continue
        elif choice == 't':
            print('execute tcpsever')
            tcpClient()
        else:
            print('execute udpsever')
            udpClient()
