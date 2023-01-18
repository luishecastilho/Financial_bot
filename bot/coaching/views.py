from django.shortcuts import render
from django.http import HttpResponse
from .models import Video

# Create your views here.

def index(request):
    #dados de um possível e necessário LOGIN
    user = []
    account = []

    videos = Video.objects.all()

    return render(request, 'coaching/index.html', {
                                                    'user': user,
                                                    'account': account,
                                                    'videos': videos
                                                })