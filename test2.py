# from alarm import*
# import threading
# import time
# def io():
#     write()
#     read()


# counts=[]
# t=time.time()
# for x in range(10):
#     # th=threading.Thread(target=count,args=(1,1))
#     th=threading.Thread(target=io)
#     counts.append(th)
#     th.start()
# for i in counts:
#     i.join()
# # print('thread cpu:',time.time()-t)
# print('thread io:',time.time()-t)

from signal import*
import os 
import sys
import multiprocessing

def saler_handler(signum,frame):
    if signum==SIGINT:
        os.kill(os.getppid(),SIGUSR1)
    elif signum==SIGQUIT:
        os.kill(os.getppid(),SIGUSR2)
    elif signum==SIGUSR1:
        print('到站了，下车')
        sys.exit('saler 下车了')
def driver_handler(signum,frame):
    if signum==SIGUSR1:
        print('开车了开车了．．．')
    elif signum==SIGUSR2:
        print('停车．．．．')
    elif signum==SIGTSTP:
        os.kill(p.pid,SIGUSR1)

def saler():
    signal(SIGINT,saler_handler)
    signal(SIGQUIT,saler_handler)
    signal(SIGUSR1,saler_handler)
    signal(SIGTSTP,SIG_IGN)
    while True:
        pass

p=multiprocessing.Process\
    (name='zhangjie',target=saler)
p.start()

signal(SIGUSR1,driver_handler)
signal(SIGUSR2,driver_handler)
signal(SIGTSTP,driver_handler)
signal(SIGINT,SIG_IGN)
signal(SIGQUIT,SIG_IGN)

p.join()








