from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *

menu = ['Головна', 'Товари', 'Додати товар', 'Контакти']

def main_page(request):
    goods = Goods.objects.all()
    return render(request, 'shop/main_page.html', {'goods': goods, 'menu': menu, 'title': 'Головна'})


def categories(request, cat):
    return HttpResponse(f"<h1>Відображення товарів за категоріями</h1><p>{cat}</p>")


def goods(request):
    item = Goods.objects.all()
    return render(request, 'shop/goods.html', {'item': item, 'menu': menu, 'title': 'Товари магазину'})

def goods_checklist(request):
    return render(request, 'shop/goods_checklist.html')

def pageNotFound(request, exceprion):
    return HttpResponseNotFound('Сторінка не знайдена')