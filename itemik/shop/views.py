from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *

menu = ['Головна', 'Товари', 'Додати товар']

def index(request):
    goods = Goods.objects.all()
    return render(request, 'shop/index.html', {'goods': goods, 'menu': menu, 'title': 'Головна'})


def item(request):
    return render(request, 'shop/item.html')


def categories(request, cat):
    return HttpResponse(f"<h1>Відображення товарів за категоріями</h1><p>{cat}</p>")


def goods(request):
    item = Goods.objects.all()
    return render(request, 'shop/goods.html', {'item': item, 'menu': menu, 'title': 'Товари магазину'})

def goods_checklist(request):
    return render(request, 'shop/goods_checklist.html')


def profile(request):
    user = Goods.objects.all()
    return render(request, 'shop/profile.html', {'user': user, 'menu': menu, 'title': 'Мій профіль'})

def pageNotFound(request, exceprion):
    return HttpResponseNotFound('Сторінка не знайдена')