from django.shortcuts import render

from .models import Products, Categories


def catalog(request):

    goods = Products.objects.all()

    categories = Categories.objects.all()

    context = {
        'title': 'Home - Каталог',
        'goods': goods,
        'categories': categories,

    }

    return render(request, 'goods/catalog.html', context)


def product(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home - товары',
        'categories': categories
    }

    return render(request, 'goods/product.html', context)
