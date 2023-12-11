from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth import logout, login

from .forms import LoginUserForm, RegisterUserForm
from .models import *
from .utils import DataMixin

menu = [{'title': 'Головна', 'url_name': 'main_page'},
        {'title': 'Мої замовлення', 'url_name': 'main_page'},
]


navigation_menu = [
    {'id': 1, 'name': 'Мій профіль'},
    {'id': 2, 'name': 'Мої замовлення'},
    {'id': 3, 'name': 'Категорії товарів'},
    {'id': 4, 'name': 'Увійти'},
]


class ShopHome(DataMixin, ListView):
    model = Goods
    template_name = 'shop/index.html'
    context_object_name = 'goods'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
# def index(request):
#     goods = Goods.objects.all()
#     return render(request, 'shop/index.html', {'goods': goods, 'menu': menu, 'title': 'Головна'})
#


def item(request):
    itemik = Goods.objects.all()
    return render(request, 'shop/item.html', context={'item': itemik, 'title': 'Товар'})


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
    info = Profile.objects.all()
    return render(request, 'shop/profile.html', {'info': info, 'menu': menu, 'title': 'Мій профіль'})

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Реєстрація")
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'shop/log_in.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизація")
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('main_page')

def login(request):
    login = Goods.objects.all()
    return render(request, 'shop/log_in.html', {'login': login, 'menu': menu, 'title': 'Авторизація'})


def logout_user(request):
    logout(request)
    return redirect('login_user')


def pageNotFound(request, exceprion):
    return HttpResponseNotFound('Сторінка не знайдена')