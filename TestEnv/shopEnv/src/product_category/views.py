from django.shortcuts import render
from .models import Product

# import all model(s)
# from .models import *

# Create your views here.
def basePage(request):
  context = {}
  return render(request, 'product_category/base.html', context)

def homePage(request):
  context = {}
  return render(request, 'product_category/home.html', context)

def jeansPage(request):
  # obj = Product.objects.all()
  # print(obj)
  obj = Product.objects.filter(category='jeans')
  context = { 
    'object': obj
  }
  return render(request, 'product_category/jeans.html', context)

def shirtsPage(request):
  obj = Product.objects.filter(category='shirts')
  context = { 
    'object': obj
  }
  return render(request, 'product_category/shirts.html', context)

def sweatsPage(request):
  queryset = Product.objects.filter(category='sweats')
  context = { 
    'object_list': queryset
  }
  return render(request, 'product_category/sweats.html', context)

def coatsPage(request):
  obj = Product.objects.filter(category='coats')
  context = { 
    'object': obj
  }
  return render(request, 'product_category/coats.html', context)

def product_details(request, id):
  obj = Product.objects.get(id=id)
  context = { 
    'object': obj
  }
  return render(request, 'product_category/product_details.html', context)

def cartPage(request):
  context = {}
  return render(request, 'product_category/cart.html', context)

def checkoutPage(request):
  context = {}
  return render(request, 'product_category/checkout.html', context)