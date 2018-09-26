from socket import *
from multiprocessing import Process
import os
import sys
import time


HOST = '0.0.0.0'
PORT = 12345
ADDR = (HOST, PORT)
FPATH = 'home/tarena/mydata/'
class FtpServer():
    pass

def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)

    while True:
        connfd, addr = sockfd.accept()
        


if __name__ == '__main__':
    main()

