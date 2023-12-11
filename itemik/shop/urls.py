from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('', goods, name='main_page'),
    path('index/', ShopHome.as_view()),
    path('category/<slug:cat>', categories),  # маршрут - http://127.0.0.1:8000/category/...
    #path('', ShopHome.as_view(), name='main_page'),
    path('item/', item, name='item'),
    path('goods_checklist/', goods_checklist),
    path('my_orders/', my_orders, name='orders'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_user, name='logout'),
    path('login/', LoginUser.as_view(), name='login_user'),
    #path('category/<int:cat_id>/', show_category, name='category'),
    #just review materials by Git-Hub
]