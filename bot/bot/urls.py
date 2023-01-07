from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'Apresentação e escolha do BOT'),
    path('execution/', views.execution, name = 'Execução do BOT')
]