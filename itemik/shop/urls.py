from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('', index, name='main_page'),
    path('category/<slug:cat>', categories),  # маршрут - http://127.0.0.1:8000/category/...
    path('goods/', goods),
    path('item/', item, name='item'),
    path('goods_checklist/', goods_checklist),
    path('my_orders/', my_orders, name='orders'),
    path('profile/', profile, name='profile'),
    path('login/', login, name='login_user'),
    #path('category/<int:cat_id>/', show_category, name='category'),
    #just review materials by Git-Hub
]