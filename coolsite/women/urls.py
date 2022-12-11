from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'), #http://127.0.0.1:8000/
    path('category/<int:catid>/', categories), #http://127.0.0.1:8000/category/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive), #использование регулярного выражения
    path('about/', about, name='about'),
]