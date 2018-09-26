from socket import *
import time


class FtpClient(s):
    def __init__(self, s):
        self.s = s

    def check_file():
        s.send("C ".encode())
        data = s.recv(4096)




def showitem():
    print("--------------------")
    print("----- 1:check ------")
    print("----- 2:get file ---")
    print("----- 3:put file ---")
    print("----- q:exit -------")
    print("--------------------")

def main():
    s = socket()
    s.connect("127.0.0.1",12345)
    ftp = FtpClient(s)
    while True:
        show_item()
        enter = input("请输入命令：")
        if enter == '1':
            ftp.check_file()s
        elif enter == '2':
            pass

if __name__ == '__main__':
    main()









