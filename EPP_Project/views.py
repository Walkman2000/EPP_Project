from django.shortcuts import render, HttpResponse, redirect
from EPP.models import Productos
from django.db import connection

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

def agregar_productos(request):
    cursor = connection.cursor()
    clientes = cursor.execute("SELECT * FROM Clientes")
    print("Clientes:",clientes.fetchall())

    return render(request, 'productos.html',{
        'clientes':clientes
    })