from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='main_page'),
    path('category/<slug:cat>', categories),  # маршрут - http://127.0.0.1:8000/category/...
    path('goods/', goods),
    path('item/', item, name='item'),
    path('goods_checklist/', goods_checklist),
    path('profile/', profile, name='profile')
    #just review materials by Git-Hub
]