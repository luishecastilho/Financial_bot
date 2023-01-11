from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'contact'),
    path('send', views.send, name = 'send')
]