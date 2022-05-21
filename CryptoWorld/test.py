# 3C75DCE2-F4BA-453C-8869-4D8317BE29AF
# https://cryptoicons.org/api/icon/eth/200
import json
import requests
from coinbase.wallet.client import Client
import datetime
url = 'https://rest.coinapi.io/v1/assets/icons/1'
headers = {'X-CoinAPI-Key' : '3C75DCE2-F4BA-453C-8869-4D8317BE29AF'}
client = Client("AzkHUVwGrcoUlAxH", "jlKeLnhFX4nIbKy7MrG1UDizQmEiE0c7")
response = requests.get(url, headers=headers)
# print((response.text))
def printCurrency() :
    currencies = client.get_currencies()
    currenciesjson = json.dumps(currencies)
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
print(getBTC('05-20-2022 19:59:26'))
# for i in range(0, 7):
#     print(getBTC(datetime.datetime.now() - datetime.timedelta(i)).amount)
