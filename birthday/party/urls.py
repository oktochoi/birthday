from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='main'),
    path('login/', views.login_view, name='login'),
    path('room/', views.room_view, name = 'room')
    
]
