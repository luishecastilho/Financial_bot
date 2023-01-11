from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('list/', views.list, name = 'list'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('execution/<str:id>', views.execution, name = 'execution')
]