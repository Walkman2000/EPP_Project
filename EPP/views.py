from django.shortcuts import render, HttpResponse
from django.db import connection
from .models import Productos
from django.template.exceptions import TemplateDoesNotExist, TemplateSyntaxError
# Create your views here.
def index_admin(request):
    contexto = {}
    try:
        prods =  Productos.objects.all()
        contexto["productos"] = prods
        print("Productos:", prods)
        return render(request, "admin/productos.html", contexto)
    except (TemplateDoesNotExist, TemplateSyntaxError) as e:
        print(e)
        return HttpResponse("Ocurrió un error")