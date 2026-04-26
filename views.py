from django.shortcuts import render
from .models import Cliente, Producto, Compra
from .forms import ClienteFormulario, ProductoFormulario, CompraFormulario, BuscarProductoFormulario


def inicio(request):
    formulario = BuscarProductoFormulario()
    return render(request, "tienda/inicio.html", {"formulario": formulario})


def clientes(request):
    if request.method == "POST":
        formulario = ClienteFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            cliente = Cliente(
                nombre=info["nombre"],
                correo=info["correo"],
                edad=info["edad"],
                intereses=info["intereses"]
            )
            cliente.save()
            return render(request, "tienda/clientes.html", {
                "formulario": ClienteFormulario(),
                "mensaje": "Cliente agregado correctamente"
            })
    else:
        formulario = ClienteFormulario()

    return render(request, "tienda/clientes.html", {"formulario": formulario})


def productos(request):
    if request.method == "POST":
        formulario = ProductoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            producto = Producto(
                nombre=info["nombre"],
                categoria=info["categoria"],
                precio=info["precio"],
                stock=info["stock"]
            )
            producto.save()
            return render(request, "tienda/productos.html", {
                "formulario": ProductoFormulario(),
                "mensaje": "Producto agregado correctamente"
            })
    else:
        formulario = ProductoFormulario()

    return render(request, "tienda/productos.html", {"formulario": formulario})


def compras(request):
    if request.method == "POST":
        formulario = CompraFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            compra = Compra(
                cliente=info["cliente"],
                producto=info["producto"],
                tienda=info["tienda"],
                cantidad=info["cantidad"]
            )
            compra.save()
            return render(request, "tienda/compras.html", {
                "formulario": CompraFormulario(),
                "mensaje": "Compra agregada correctamente"
            })
    else:
        formulario = CompraFormulario()

    return render(request, "tienda/compras.html", {"formulario": formulario})


def buscar_producto(request):
    if request.GET.get("categoria"):
        categoria = request.GET["categoria"]
        productos = Producto.objects.filter(categoria__icontains=categoria)
        return render(request, "tienda/resultados_busqueda.html", {
            "productos": productos,
            "categoria": categoria
        })

    return render(request, "tienda/inicio.html", {
        "formulario": BuscarProductoFormulario(),
        "mensaje": "No se ingresó ninguna categoría"
    })