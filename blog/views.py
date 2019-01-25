from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('欢迎使用Django')

# Create your views here.
