from django.shortcuts import render

from catalog.models import Product
from django.shortcuts import get_object_or_404


def product_list(request):
    product = Product.objects.all()
    context = {"product": product}
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_detail.html', context)