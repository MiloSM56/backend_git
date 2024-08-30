from django.urls import path
from . import views

urlpatterns = [
    path('', views.index3),
    path('saludo3/', views.presentacion3),
    
]
