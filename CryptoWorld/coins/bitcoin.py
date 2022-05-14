import json
from .. import consume
import time
import datetime
import threading
class Bitcoin :
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
        Bitcoin.currentData.append(float(consume.getCoin('BTC').amount))
    #print(Bitcoin.basicData)
    while(Bitcoin.active) :
        if(len(Bitcoin.currentData)>=MAXCD) :
            Bitcoin.currentData.pop(0)
            Bitcoin.currentData.append(float(consume.getCoin('BTC').amount))
        else :
            Bitcoin.currentData.append(float(consume.getCoin('BTC').amount))
        if(TODAY!=datetime.datetime.now().day) :
            Bitcoin.dayData.pop(0)
            Bitcoin.dayData.append(Bitcoin.currentData[MAXCD-1])
            TODAY=datetime.datetime.now().day
        time.sleep(60)
def b() :
    for j in range(0,MAXDD) :
        Bitcoin.dayData.append(0)
    tn=datetime.datetime.now()
    for j in range(0,MAXDD) :
        Bitcoin.dayData[MAXDD-j-1]=consume.getCoin('BTC',tn - datetime.timedelta(j)).amount
# Bitcoin.basicData=json.dumps(consume.getCoinDetails('BTC'))
    
def run() :
    ta=threading.Thread(target=a)
    tb=threading.Thread(target=b)
    tb.start()
    ta.start()