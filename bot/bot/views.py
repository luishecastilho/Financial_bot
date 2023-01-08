from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bot(request):


    
    return render(request, 'bot.html', {'text':'Apresentação e escolha do BOT"'})

def bot_execution(request):



    return render(request, 'bot_execution.html', {'text':'Execução do BOT"'})