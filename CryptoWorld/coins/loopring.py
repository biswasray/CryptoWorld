import json
from .. import consume
import time
import datetime
import threading
class Loopring :
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
        Loopring.currentData.append(float(consume.getCoin('LRC').amount))
    #print(Loopring.basicData)
    while(Loopring.active) :
        if(len(Loopring.currentData)>=MAXCD) :
            Loopring.currentData.pop(0)
            Loopring.currentData.append(float(consume.getCoin('LRC').amount))
        else :
            Loopring.currentData.append(float(consume.getCoin('LRC').amount))
        if(TODAY!=datetime.datetime.now().day) :
            Loopring.dayData.pop(0)
            Loopring.dayData.append(Loopring.currentData[MAXCD-1])
            TODAY=datetime.datetime.now().day
        time.sleep(60)
def b() :
    for j in range(0,MAXDD) :
        Loopring.dayData.append(0)
    tn=datetime.datetime.now()
    for j in range(0,MAXDD) :
        Loopring.dayData[MAXDD-j-1]=consume.getCoin('LRC',tn - datetime.timedelta(j)).amount
# Loopring.basicData=json.dumps(consume.getCoinDetails('LRC'))

def run() :
    ta=threading.Thread(target=a)
    tb=threading.Thread(target=b)
    tb.start()
    ta.start()