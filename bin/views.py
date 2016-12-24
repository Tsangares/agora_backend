from django.shortcuts import render
from bin.models import *
from django.core import serializers
import json
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse
import os
import sys
sys.path.append(os.path.abspath("/var/www/will/bot/priceindex/"))

def chart(request):
    logToJson()
    t = get_template('chart.html')
    data = open('/var/www/will/bot/priceindex/log/plot.json', 'r').read()
    html = t.render(Context({'data': data}))
    return HttpResponse(html)
def chartnew(request):
    logToJson()
    t = get_template('chart_new.html')
    data = open('/var/www/will/bot/priceindex/log/plot.json', 'r').read()
    html = t.render(Context({'data': data}))
    return HttpResponse(html)

def doc(request):
    t = get_template('docs/output.html')
    html = t.render()
    return HttpResponse(html)

def index(request):
    return HttpResponse("This is probabbly the bin.")

def test(request):
    html = "This is a test."
    return HttpResponse(html)

def search(request):
    if(request.method == 'GET'):
        query = request.GET.get('query', 'null')
    elif(request.method == 'POST'):
        query = request.POST.get('query', 'null')
    #offset = (int)request.POST.get('offest', '0')
    #limit =(int)request.POST.get('limit', '30')
    objs = Questions.objects.filter(question__search=query)
    output = {'questions':serializers.serialize("json", objs),'count':len(objs)}
    return HttpResponse(json.dumps(output),content_type="application/json")
    #return HttpResponse(len(objs))
