from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .models import Product


# Create your views here.
@login_required(login_url='/admin')
def product(request):
    return render(request,'product/welcome.html',{})


def list(request):
    all_products = Product.objects.all()
    return render(request, 'product/products_list.html',{'products':all_products})