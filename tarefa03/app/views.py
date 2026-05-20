from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def usuarios(request):
    lista_usuarios = [
        {"nome": "Michael Douglas", "matricula": "202411233234",  "idade": 23},
        {"nome": "James Wilson", "matricula": "202411234532",  "idade": 55},
        {"nome": "Peter Parker", "matricula": "201411233234", "idade": 22},
        {"nome": "Morual","matricula": "202411234634", "idade": 67},
        {"nome": "Atla", "matricula": "202321233234", "idade": 73},
        {"nome": "Zigo", "matricula": "2024157633234", "idade": 13},
        {"nome": "Mark", "matricula": "202125633234", "idade": 63},
        ]
    context = {
        "usuarios": lista_usuarios,
    }
    return render(request,'usuarios.html', context)