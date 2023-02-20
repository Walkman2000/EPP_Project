from django.shortcuts import render, HttpResponse, redirect


def index(request):
    nombre = 'roberto'

    context ={
        'nombre': nombre
    }
    return render(request, 'index.html', context)

def pedidos(request):
    pedido = 'pedido1'

    context ={
        'pedido' : pedido
    }
    return render(request, 'pedidos.html', context)