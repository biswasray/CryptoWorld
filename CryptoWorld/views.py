from turtle import color
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd  
import numpy as np    
import matplotlib.pyplot as plt
import requests
import json
# def index(req) :
#     return render(req,'index.html',{"App_name":"Crypto World"})
def coins(req) :
	# price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=INR")
	# price = json.loads(price_request.content)
    # return render(req,'coins.html',{"App_name":"Crypto World"})
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,DOGE,LRC,XRP,BNB,SOL,BUSD,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=INR")
	price = json.loads(price_request.content)
	for key,value in price["DISPLAY"].items() :
		if float(value["INR"]["CHANGEPCT24HOUR"])<0 :
			price["DISPLAY"][key]["INR"]["COLOR"]='red'
		else :
			price["DISPLAY"][key]["INR"]["COLOR"]='green'
	return render(req, 'coins.html', {"App_name":"Crypto World", 'price': price})
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
	
# def currentdata(req,cid) :
#     # return HttpResponse(json.dumps(consume.getCoinDetails(cid)))
#     return HttpResponse(consume.pipelineBasic(cid))
# def currentMinute(req,cid) :
#     return HttpResponse(consume.pipelineMinute(cid))
# def getCoin(req,cid,date) :
#     return HttpResponse(consume.getCoin(cid,date))
# def currentDays(req,cid) :
#     return HttpResponse(consume.pipelineDays(cid))
def faqs(request):
	return render(request, 'FAQs.html',{"App_name":"Frequently Asked Questions"})
def about(req) :
	return render(req, 'about.html',{"App_name":"About Us"})
def index(request):
	# Grab Crypto Price Data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,DOGE,XRP,LRC,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=INR")
	price = json.loads(price_request.content)

	return render(request, 'index.html', {"App_name":"Crypto World", 'price': price})
def news(request):
	# Grab Crypto News
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'news.html', {"App_name":"Latest News",'api': api})
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
	no=[]
	mi=0
	# print(price["Data"]["Data"][0]["open"])
	for i in range(1,len(price["Data"]["Data"])) :
		t=(100*(price["Data"]["Data"][i]["open"]-price["Data"]["Data"][i-1]["open"]))/price["Data"]["Data"][i-1]["open"]
		perc.append(t)
		no.append(mi)
		mi=mi+1
	data={"No":no,"Perc":perc}
	return HttpResponse(predict(pd.DataFrame(data)))
def predict(data_load) :
	data_load.head(6)
	data_load.plot(x='No', y='Perc', style='o')   
	X = data_load.iloc[:, :-1].values    
	y = data_load.iloc[:, 1].values
	from sklearn.model_selection import train_test_split    
	X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=0)
	from sklearn.linear_model import LinearRegression    
	regressor = LinearRegression()    
	regressor.fit(X_train, y_train) 
	line = regressor.coef_*X+regressor.intercept_ 
	y_pred = regressor.predict(X_test)
	df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})    
	df
	hours = [[365]]  
	own_pred = regressor.predict(hours) 
	return own_pred[0]