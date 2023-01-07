from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):


    
    return render(request, 'index.html', {'text':'Apresentação e escolha do BOT"'})

def execution(request):



    return render(request, 'execution.html', {'text':'Execução do BOT"'})