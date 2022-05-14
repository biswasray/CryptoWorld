import json
from .. import consume
import time
import datetime
import threading
class Ethereum :
    currentData=[]
    dayData=[]
    basicData=""
    active=True
MAXCD=60
MAXDD=365
TODAY=datetime.datetime.now().day
def a() :
    TODAY=datetime.datetime.now().day
    for i in range(0,60):
        Ethereum.currentData.append(float(consume.getCoin('ETH').amount))
    #print(Ethereum.basicData)
    while(Ethereum.active) :
        if(len(Ethereum.currentData)>=MAXCD) :
            Ethereum.currentData.pop(0)
            Ethereum.currentData.append(float(consume.getCoin('ETH').amount))
        else :
            Ethereum.currentData.append(float(consume.getCoin('ETH').amount))
        if(TODAY!=datetime.datetime.now().day) :
            Ethereum.dayData.pop(0)
            Ethereum.dayData.append(Ethereum.currentData[MAXCD-1])
            TODAY=datetime.datetime.now().day
        time.sleep(60)
def b() :
    for j in range(0,MAXDD) :
        Ethereum.dayData.append(0)
    tn=datetime.datetime.now()
    for j in range(0,MAXDD) :
        Ethereum.dayData[MAXDD-j-1]=consume.getCoin('ETH',tn - datetime.timedelta(j)).amount
# Ethereum.basicData=json.dumps(consume.getCoinDetails('ETH'))
    
def run() :
    ta=threading.Thread(target=a)
    tb=threading.Thread(target=b)
    tb.start()
    ta.start()