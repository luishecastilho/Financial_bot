from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import deriv
import asyncio

def index(request):
    #dados de um possível LOGIN
    user = []
    return render(request, 'bot/index.html', {'user': user})

def list(request):    
    account = asyncio.run(deriv.getCache())
    return render(request, 'bot/list.html', {'account': account})

def login(request):
    # AQUI TEM QUE SER O LOGIN DO SISTEMA


    #if request.GET.get('type') not in ['real','fake']:
        #return HttpResponse('Erro ao fazer o LOGIN', content_type='text/plain', status=400)
    try:
        #account = asyncio.run(deriv.login(request.GET.get('type')))
        account = []
    except Exception as e:
        return HttpResponse(str(e), content_type='text/plain', status=400)

    return HttpResponseRedirect('/bot/list/')

def logout(request):
    # AQUI TEM QUE SER O LOGOUT DO SISTEMA
    #asyncio.run(deriv.logout())
    
    return HttpResponseRedirect('/bot/')

def execution(request, id):
    account = asyncio.run(deriv.getCache())
    return render(request, 'bot/execution.html', {'account': account, 'id': id})