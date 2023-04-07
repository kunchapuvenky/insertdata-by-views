from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from app.models import *

def Topic_insert(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic data inserted successfully.')

def Webpage_insert(request):
    tn=input('enter topic_name')
    n=input('enter name')
    url=input('enter url')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    return HttpResponse('webpage data inserted successfully')

def AccessRecord_insert(request):
    tn=input('enter topic_name') 
    n=input('enter name')
    url=input('enter url')
    a=input('enter author')
    d=input('enter date')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    AR=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    AR.save()
    return HttpResponse('AccessRecord data inserted.')