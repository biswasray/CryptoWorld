# https://api.nomics.com/v1/currencies/ticker?key=e450a2e5cc8e1372c119020361f72e70acd3d9f0&ids=BTC,ETH,XRP&interval=1d,30d&convert=EUR&platform-currency=ETH&per-page=100&page=1
# coinbase
# api-key: AzkHUVwGrcoUlAxH
# api-secret: jlKeLnhFX4nIbKy7MrG1UDizQmEiE0c7
import json
import requests
from coinbase.wallet.client import Client
import ast
import time

from CryptoWorld.coins.ethereum import Ethereum
from CryptoWorld.coins.bitcoin import Bitcoin
from CryptoWorld.coins.ethereumClassic import EthereumClassic
from CryptoWorld.coins.doge import Doge
from CryptoWorld.coins.loopring import Loopring
import CryptoWorld.coins.ripple as Ripple
#url = 'https://rest.coinapi.io/v1/assets/'
headers = {'X-CoinAPI-Key' : '3C75DCE2-F4BA-453C-8869-4D8317BE29AF'}
client = Client("AzkHUVwGrcoUlAxH", "jlKeLnhFX4nIbKy7MrG1UDizQmEiE0c7")
# var={
#     'roll':1,
#     'name':"Sbr"
# }
def printCurrency() :
    currencies = client.get_currencies()
    currenciesjson = json.dumps(currencies)
    # print(currencies.data)
printCurrency()
def getCurrency(id) :
    currencies = client.get_currencies()
    for x in currencies.data :
        if x.id == id:
            return x
    return None
def getBTC(date=None) :
    if date==None :
        return client.get_spot_price(currency_pair='BTC-INR')
    return client.get_spot_price(currency_pair='BTC-INR',date=date)
def getCoin(coinname,date=None) :
    if date==None :
        return client.get_spot_price(currency_pair=(coinname+'-INR'))
    return client.get_spot_price(currency_pair=(coinname+'-INR'),date=date)
#print(getBTC('2018-06-23T18:02:51Z'))
def getCoinDetails(coinname) :
    url='https://rest.coinapi.io/v1/assets/'+coinname.lower()
    response = requests.get(url, headers=headers)
    temp=ast.literal_eval(response.text)
    result=temp[0]
    price=(dict(getCoin(coinname)))
    result["currency"]=price["currency"]
    result["amount"]=price["amount"]
    return (result)
def pipelineBasic(id) :
    if(id=='XRP') :
        return json.dumps(getCoinDetails('BTC'))
    return json.dumps(getCoinDetails(id))
    #print(Ethereum.basicData)
    # if(id=='ETH') :
    #     return json.dumps(getCoinDetails('ETH'))
    # elif(id=='BTC') :
    #     return json.dumps(getCoinDetails('BTC'))
    # elif(id=='ETC') :
    #     return json.dumps(getCoinDetails('ETH'))
    # elif(id=='DOGE') :
    #     return json.dumps(getCoinDetails('ETH'))
    # elif(id=='LRC') :
    #     return json.dumps(getCoinDetails('ETH'))
    # return None
def pipelineMinute(id) :
    if(id=='ETH') :
        return json.dumps(Ethereum.currentData)
    elif(id=='BTC') :
        return json.dumps(Bitcoin.currentData)
    elif(id=='ETC') :
        return json.dumps(EthereumClassic.currentData)
    elif(id=='DOGE') :
        return json.dumps(Doge.currentData)
    elif(id=='LRC') :
        return json.dumps(Loopring.currentData)
    elif(id=='XRP') :
        return json.dumps(Ripple.dayBefore())
    return None
async def pipelineDays(id) :
    if(id=='ETH') :
        return json.dumps(Ethereum.dayData)
    elif(id=='BTC') :
        return json.dumps(Bitcoin.dayData)
    elif(id=='ETC') :
        return json.dumps(EthereumClassic.dayData)
    elif(id=='DOGE') :
        return json.dumps(Doge.dayData)
    elif(id=='LRC') :
        return json.dumps(Loopring.dayData)
    elif(id=='XRP') :
        return json.dumps(Ripple.dayBefore())
    return None
# print(getCoinDetails('ETC'))
#print(getCoin('ETC'))