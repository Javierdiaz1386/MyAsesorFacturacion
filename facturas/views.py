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

@csrf_exempt
def facturar(request):
    clientes = Cliente.objects.all()
    facturaHEAD = FacturaHead(request.POST)
    factura = FacturaDetail(request.POST)
    
    if(request.method == 'POST' and len(request.POST)<3):
        facturaHEAD = FacturaHead(request.POST)
        facturaHEAD.save()
    elif(request.method == 'POST'):
            cantidades = request.POST.getlist('cantidad')
            factura_ids = request.POST.getlist('facturaID')
            producto_ids = request.POST.getlist('ProductoID')
            print(producto_ids, request.POST)
            for p in range(0, len(cantidades)):
                factura = FacturaDetail({
                    "cantidad" : cantidades[p],
                    "facturaID" : factura_ids[p],
                    "ProductoID" : producto_ids[p],
                })
                factura.save()

    return render(request, 'paginas/facturas/facturar.html', {"clientes": clientes,
                                                              "factura": factura,
                                                              "head": facturaHEAD
                                                              })