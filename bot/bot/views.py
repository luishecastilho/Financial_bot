from django.shortcuts import render
from django.http import HttpResponse
from deriv_api import DerivAPI
from . import deriv
import asyncio
# Create your views here.

def bot(request):

    asyncio.run(deriv.sample_calls())
    
    return render(request, 'bot.html', {'text': 'testandoo'})

def bot_execution(request):



    return render(request, 'bot_execution.html', {'text':'Execução do BOT'})