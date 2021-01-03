from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.newProducts.addProducts.forms import ProductForm
from apps.newProducts.addProducts.models import Products

# Create your views here.


def index(request):
    return render(request, 'addProducts/index.html')


def product_list(request):
    product = Products.objects.all().order_by('id')
    context = {'products': product}
    return render(request, 'products/list_products.html', context)


def product_edit(request, id_product):
    product = Products.objects.get(id=id_product)
    if request.method == 'GET':
        form = ProductForm(instance=product)
    else:
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect('/listProducts')
    return render(request, 'addProducts/index.html', {'form': form})


def product_delete(request, id_product):
    product = Products.objects.get(id=id_product)
    if request.method == 'POST':
        product.delete()
        return redirect("/listProducts")
    return render(request, 'addProducts/delete_product.html', {'product': product})


def product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listProducts')
    else:
        form = ProductForm()

    return render(request, 'addProducts/index.html', {'form': form})
