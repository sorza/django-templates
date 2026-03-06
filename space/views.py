from django.shortcuts import render

def index(request):
    return render(request, 'space/index.html')

def galeria(request):
    return render(request, 'space/imagem.html')