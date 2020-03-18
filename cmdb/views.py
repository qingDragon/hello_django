from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def login(request):
    f = open('templates/login.html','r',encoding='utf-8')
    data = f.read()
    f.close()
    return HttpResponse(data)

def home(request):
    return HttpResponse('<h1>From CMDB</h1>')
