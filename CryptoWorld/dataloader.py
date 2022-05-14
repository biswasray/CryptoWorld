import threading
import time
from .coins import ethereum,bitcoin,doge,ethereumClassic,loopring

# from collections import deque
# def a() :
#     for i in range(0,9) :
#         print("a",i)
#         #time.sleep(1)
# def b() :
#     for i in range(0,9) :
#         print("b",i)
#         time.sleep(1)
def start() :
    t=[]
    t.append(threading.Thread(target=ethereum.run))
    t.append(threading.Thread(target=bitcoin.run))
    t.append(threading.Thread(target=ethereumClassic.run))
    t.append(threading.Thread(target=doge.run))
    t.append(threading.Thread(target=loopring.run))
    for th in t:
        th.start()
    
    