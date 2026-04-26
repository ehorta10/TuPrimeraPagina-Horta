from django.urls import path
from .views import inicio, clientes, productos, compras, buscar_producto

urlpatterns = [
    path('', inicio, name='inicio'),
    path('clientes/', clientes, name='clientes'),
    path('productos/', productos, name='productos'),
    path('compras/', compras, name='compras'),
    path('buscar-producto/', buscar_producto, name='buscar_producto'),
]