from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index4(request):
    return HttpResponse("<h1>Soy el index de la app2</h1>")


def presentacion4(request):
    html="""
        <h1 style="color:red">Soy un titulo de la app2.</h1>
        <h2 style="color:blue">Soy un subtitulo de la app2</h2>
        v<iframe width="560" height="315" src="https://www.youtube.com/embed/bv__9O5CZok?si=XnA5OOY_f9QOrvjQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    """
    return HttpResponse(html)