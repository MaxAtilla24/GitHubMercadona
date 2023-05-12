from django.urls import path

from . import views

urlspatterns = [
    path('product',views.product),
    #path('products_list', views.list),
   
]