from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def coaching(request):
    return render(request, 'coaching.html')