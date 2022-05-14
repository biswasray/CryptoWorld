import json
from .. import consume
import time
import datetime
import threading
class Doge :
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
        Doge.currentData.append(float(consume.getCoin('DOGE').amount))
    #print(Doge.basicData)
    while(Doge.active) :
        if(len(Doge.currentData)>=MAXCD) :
            Doge.currentData.pop(0)
            Doge.currentData.append(float(consume.getCoin('DOGE').amount))
        else :
            Doge.currentData.append(float(consume.getCoin('DOGE').amount))
        if(TODAY!=datetime.datetime.now().day) :
            Doge.dayData.pop(0)
            Doge.dayData.append(Doge.currentData[MAXCD-1])
            TODAY=datetime.datetime.now().day
        time.sleep(60)
def b() :
    for j in range(0,MAXDD) :
        Doge.dayData.append(0)
    tn=datetime.datetime.now()
    for j in range(0,MAXDD) :
        Doge.dayData[MAXDD-j-1]=consume.getCoin('DOGE',tn - datetime.timedelta(j)).amount
# Doge.basicData=json.dumps(consume.getCoinDetails('DOGE'))
    
def run() :
    ta=threading.Thread(target=a)
    tb=threading.Thread(target=b)
    tb.start()
    ta.start()