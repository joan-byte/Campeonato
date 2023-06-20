
from django.urls import path
from . import views # importamos las vistas de la aplicación

urlpatterns = [
    path('', views.hello, name='hello'),
]
    
