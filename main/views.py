from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories
    }

    return render(request, 'main/index.html', context)


def about(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Мы, компания Home заботимся о вашем уюте. '
                        'Home - одна из крупнейших компаний на рынке производства мебели для дома и офиса',
        'categories': categories
    }

    return render(request, 'main/about.html', context)
