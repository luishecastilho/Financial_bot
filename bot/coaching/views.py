from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #dados de um possível LOGIN
    user = []

    return render(request, 'coaching/index.html', {'user': user})