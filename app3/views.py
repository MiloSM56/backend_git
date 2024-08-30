from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index3(request):
    return HttpResponse("<h1>Soy el index de la app3</h1>")


def presentacion3(request):
    html="""
        <h1 style="color:red">Soy un titulo de la app3.</h1>
        <h2 style="color:green">Soy un subtitulo de la app3</h2>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/iQN0z6MDrEY?si=nuzoinbB382SQsbx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    """
    return HttpResponse(html)


