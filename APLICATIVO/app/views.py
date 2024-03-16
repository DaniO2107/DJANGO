from django.shortcuts import render
from .models import persona

def lista_personas(request):
    personas = persona.objects.all()
    return render(request, 'myapp/lista_productos.html', {'persona': personas})

