from .. import consume
import datetime
MAXCD=24*60
MAXDD=365
def yearBefore() :
    tn=datetime.datetime.now()
    temp=[]
    for j in range(0,MAXDD) :
        temp.append(0)
    for j in range(0,MAXDD) :
        temp[MAXDD-j-1]=consume.getCoin('BTC',tn - datetime.timedelta(j)).amount
    return temp
def dayBefore() :
    tn=datetime.datetime.now()
    temp=[]
    # print("temp")
    for j in range(0,50) :
        temp.append(0)
    for j in range(0,50) :
        temp[50-j-1]=consume.getCoin('BTC',tn - datetime.timedelta(hours=j)).amount
    print(temp)
    return temp
# Ripple.basicData=json.dumps(consume.getCoinDetails('XRP'))