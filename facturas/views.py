from django.shortcuts import render
from django.http import HttpResponse
from .forms import ClientForm, CrearProducto, FacturaDetail, FacturaHead
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *

def home(request):
    if(request.method == 'GET'):
        return render(request, 'index.html')

@csrf_exempt
def create_user(request):
    client_to_create = ClientForm(request.POST)
    if(request.method== 'POST'):
        if(client_to_create.is_valid()):
            client_to_create.save()
        
    return render(request, 'paginas/clientes/crear_cliente.html', {"formulario":client_to_create})

@csrf_exempt
def crear_producto(request):
    producto_a_crear = CrearProducto(request.POST)
    if(request.method == 'POST'):
        if(producto_a_crear.is_valid()):
            producto_a_crear.save()
    return render(request, 'paginas/inventario/crear_product.html', {"formulario":producto_a_crear})

def facturar(request):
    clientes = Cliente.objects.all()
    facturaHEAD = FacturaHead(request.POST)
    factura = FacturaDetail(request.POST)
    return render(request, 'paginas/facturas/facturar.html', {"clientes": clientes,
                                                              "factura": factura,
                                                              "head": facturaHEAD
                                                              })