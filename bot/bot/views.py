from django.shortcuts import render
#from django.http import HttpResponse
from . import deriv
import asyncio

def bot(request):

    return render(request, 'bot.html')

def bot_execution(request):
    account = asyncio.run(deriv.login())
    
    return render(request, 'bot_execution.html', {'account': account})