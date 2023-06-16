from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    dados = {
        1: {"nome": "Nebulosa de Carina",
            "legenda": "webbtelescope.org / NASA / James Webb"},
        2: {"nome": "Galáxia NGC 1979",
            "legenda": "nasa.or / NASA / Hubble"}
    }
    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')