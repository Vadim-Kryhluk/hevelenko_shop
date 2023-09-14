from django.urls import path

from .views import *

urlpatterns = [
    path('', main_page),
    path('category/<slug:cat>', categories),  # маршрут - http://127.0.0.1:8000/category/...
    path('goods/', goods),
    path('goods_checklist/', goods_checklist),

]