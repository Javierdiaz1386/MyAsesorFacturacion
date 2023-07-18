
from facturas import views
from django.urls import path, include

urlpatterns = [
               path('crear_cliente/', views.create_user, name='crear_liente'),
               path('inventario/crear_producto/', views.crear_producto, name='crear_producto'),
               path('facturar/', views.facturar, name='facturar')

               ]