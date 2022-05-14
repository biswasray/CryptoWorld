import json
from .. import consume
import time
import datetime
import threading
class EthereumClassic :
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
        EthereumClassic.currentData.append(float(consume.getCoin('ETC').amount))
    #print(EthereumClassic.basicData)
    while(EthereumClassic.active) :
        if(len(EthereumClassic.currentData)>=MAXCD) :
            EthereumClassic.currentData.pop(0)
            EthereumClassic.currentData.append(float(consume.getCoin('ETC').amount))
        else :
            EthereumClassic.currentData.append(float(consume.getCoin('ETC').amount))
        if(TODAY!=datetime.datetime.now().day) :
            EthereumClassic.dayData.pop(0)
            EthereumClassic.dayData.append(EthereumClassic.currentData[MAXCD-1])
            TODAY=datetime.datetime.now().day
        time.sleep(60)
def b() :
    for j in range(0,MAXDD) :
        EthereumClassic.dayData.append(0)
    tn=datetime.datetime.now()
    for j in range(0,MAXDD) :
        EthereumClassic.dayData[MAXDD-j-1]=consume.getCoin('ETC',tn - datetime.timedelta(j)).amount
# EthereumClassic.basicData=json.dumps(consume.getCoinDetails('ETC'))

def run() :
    ta=threading.Thread(target=a)
    tb=threading.Thread(target=b)
    tb.start()
    ta.start()