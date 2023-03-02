from django.shortcuts import render, HttpResponse, redirect
from EPP.models import Productos


def index(request):
    queryset = Productos.objects.all()
    return render(request, 'index.html', {'queryset':queryset})

def pedidos(request):
    pedido = 'pedido1'

    context ={
        'pedido' : pedido
    }
    return render(request, 'pedidos.html', context)

def register(request):
    
    return render(request, 'register.html')