from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(request): # view 만들기
    return render(request, 'accountapp/hello_world.html')

