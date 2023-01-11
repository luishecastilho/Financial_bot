from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #dados de um possível LOGIN
    user = []

    return render(request, 'contact/index.html', {'user': user})

def send(request):
    # request.POST.get('name')

    return HttpResponse('fas', status=200)