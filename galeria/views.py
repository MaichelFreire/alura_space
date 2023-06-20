from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia
from django.http import HttpResponse



def index(request):
    Fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {"cards": Fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})