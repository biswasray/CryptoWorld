import json
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from . import consume

def index(req) :
    return render(req,'index.html',{"App_name":"Crypto World"})
def coins(req) :
    return render(req,'coins.html',{"App_name":"Crypto World"})
def coin(req,cid) :
    return render(req,'coin.html',{"coin_name":cid})
def currentdata(req,cid) :
    # return HttpResponse(json.dumps(consume.getCoinDetails(cid)))
    return HttpResponse(consume.pipelineBasic(cid))
def currentMinute(req,cid) :
    return HttpResponse(consume.pipelineMinute(cid))
def getCoin(req,cid,date) :
    return HttpResponse(consume.getCoin(cid,date))
def currentDays(req,cid) :
    return HttpResponse(consume.pipelineDays(cid))