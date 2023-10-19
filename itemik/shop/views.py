from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': 'Головна', 'url_name': 'main_page'},
        {'title': 'Мої замовлення', 'url_name': 'main_page'},
]


navigation_menu = [
    {'id': 1, 'name': 'Мій профіль'},
    {'id': 2, 'name': 'Мої замовлення'},
    {'id': 3, 'name': 'Категорії товарів'},
    {'id': 4, 'name': 'Увійти'},
]




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


#def show_category(request, cat_id):
    #return index(request)

def my_orders(request):
    order = Goods.objects.all()
    return render(request, 'shop/my_orders.html', {'order': order, 'menu': menu, 'title': 'Мої замовлення'})


def profile(request):
    user = Goods.objects.all()
    return render(request, 'shop/profile.html', {'user': user, 'menu': menu, 'title': 'Мій профіль'})

def login(request):
    login = Goods.objects.all()
    return render(request, 'shop/log_in.html', {'login': login, 'menu': menu, 'title': 'Авторизація'})


def pageNotFound(request, exceprion):
    return HttpResponseNotFound('Сторінка не знайдена')