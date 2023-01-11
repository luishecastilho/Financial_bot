from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import deriv
import asyncio

def index(request):
    account = asyncio.run(deriv.getCache())
    return render(request, 'bot/index.html', {'account': account})

def list(request):    
    account = asyncio.run(deriv.getCache())
    return render(request, 'bot/list.html', {'account': account})

def login(request):
    if request.GET.get('type') not in ['real','fake']:
        return HttpResponse('Erro ao fazer o LOGIN', content_type='text/plain', status=400)
    try:
        account = asyncio.run(deriv.login(request.GET.get('type')))
    except Exception as e:
        return HttpResponse(str(e), content_type='text/plain', status=400)

    return HttpResponseRedirect('/bot/list/')

def logout(request):
    asyncio.run(deriv.logout())
    
    return HttpResponseRedirect('/bot/')

def execution(request, id):
    account = asyncio.run(deriv.getCache())
    return render(request, 'bot/execution.html', {'account': account, 'id': id})