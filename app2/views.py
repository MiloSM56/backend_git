from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index2(request):
    return HttpResponse("<h1>Soy el index de la app2</h1>")


def presentacion2(request):
    html="""
        <h1 style="color:red">Soy un titulo de la app2.</h1>
        <h2 style="color:blue">Soy un subtitulo de la app2</h2>
    """
    return HttpResponse(html)






