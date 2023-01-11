from django.shortcuts import render
#from django.http import HttpResponse
from . import deriv
import asyncio

def index(request):

    return render(request, 'bot/index.html')

def execution(request):
    account = asyncio.run(deriv.login())
    
    return render(request, 'bot/execution.html', {'account': account})