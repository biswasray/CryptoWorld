from turtle import color
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from . import consume
import requests
import json
# def index(req) :
#     return render(req,'index.html',{"App_name":"Crypto World"})
def coins(req) :

    return render(req,'coins.html',{"App_name":"Crypto World"})
def coin(req,cid) :
	cid=cid.upper()
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+cid+"&tsyms=INR")
	price = json.loads(price_request.content)
	color='black'
	if((float(price["DISPLAY"][cid]["INR"]["CHANGEPCT24HOUR"]))<0) :
		color='red'
	else :
		color='green'
	return render(req, 'coin.html', {"App_name":"Crypto World","coin_name":cid,"color":color, 'crypto': price})
	
def currentdata(req,cid) :
    # return HttpResponse(json.dumps(consume.getCoinDetails(cid)))
    return HttpResponse(consume.pipelineBasic(cid))
def currentMinute(req,cid) :
    return HttpResponse(consume.pipelineMinute(cid))
def getCoin(req,cid,date) :
    return HttpResponse(consume.getCoin(cid,date))
def currentDays(req,cid) :
    return HttpResponse(consume.pipelineDays(cid))
def index(request):
	# Grab Crypto Price Data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=INR")
	price = json.loads(price_request.content)

	# Grab Crypto News
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'index.html', {"App_name":"Crypto World",'api': api, 'price': price})
def dailyHistory(req,cid) :
	return HttpResponse(requests.get("https://min-api.cryptocompare.com/data/v2/histoday?fsym="+cid+"&tsym=INR&limit=365"))
def hourlyHistory(req,cid) :
	return HttpResponse(requests.get("https://min-api.cryptocompare.com/data/v2/histohour?fsym="+cid+"&tsym=INR&limit=24"))
def minuteHistory(req,cid) :
	return HttpResponse(requests.get("https://min-api.cryptocompare.com/data/v2/histominute?fsym="+cid+"&tsym=INR&limit=60"))
def coindetails(req,cid) :
	return HttpResponse(requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+cid+"&tsyms=INR"))
def dailyPercent(req,cid) :
	price_request = requests.get("https://min-api.cryptocompare.com/data/v2/histoday?fsym="+cid+"&tsym=INR&limit=365")
	price = json.loads(price_request.content)
	perc=[]
	print(price["Data"]["Data"][0]["open"])
	for i in range(1,len(price["Data"]["Data"])) :
		t=(100*(price["Data"]["Data"][i]["open"]-price["Data"]["Data"][i-1]["open"]))/price["Data"]["Data"][i-1]["open"]
		perc.append(t)
	return HttpResponse(json.dumps(perc))