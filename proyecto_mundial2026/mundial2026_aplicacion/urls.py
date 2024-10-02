from django.urls import path
from .views import home, index, calendario, equipos, jugadores, login, perfil, registro, tecnicos

urlpatterns = [
    path('', home, name='home'),      
    path('index/', index, name='index'),  
    path('calendario/', calendario, name='calendario'),  
    path('equipos/', equipos, name='equipos'),  
    path('jugadores/', jugadores, name='jugadores'),  
    path('login/', login, name='login'),  
    path('perfil/', perfil, name='perfil'),
    path('registro/', registro, name='registro'),  
    path('tecnicos/', tecnicos, name='tecnicos'),
]
