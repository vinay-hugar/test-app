from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def about(request):
    return render(request,'generator/about.html')

def home(request):
    return render(request,'generator/home.html',{'password':'kdhbcdhbcdbhbd'})

def eggs(request):
    return HttpResponse('<h1>Hey Eggs!<hq>')

def password(request):
    thepassword=''
    characters=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get('length',12))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend('!@#$%^&*')
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    for x in range(length):
        thepassword+=random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})
