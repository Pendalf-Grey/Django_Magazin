from django.shortcuts import render
from .models import Products


def catalog(request):
    goods = Products.objects.all()

    context = {
        'title': 'Home - Каталог',
        'goods': goods,

    }

    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    one_product = Products.objects.get(slug=product_slug)

    context = {
        'title': 'Home - товары',
        'product': one_product,
    }

    return render(request, 'goods/product.html', context=context)
