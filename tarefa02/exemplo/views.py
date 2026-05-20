from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def outra(request):
    return render(request, "outra.html" )
