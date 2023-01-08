from django.urls import path
from . import views


urlpatterns = [
    path('', views.bot, name = 'Apresentação e escolha do BOT'),
    path('execution/', views.bot_execution, name = 'Execução do BOT')
]