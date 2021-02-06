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
  return render(request, 'product_Category/home.html', context)

def jeansPage(request):
  obj = Product.objects.all()
  context = { 
    'object': obj
   }
  return render(request, 'product_Category/jeans.html', context)

def shirtsPage(request):
  context = {}
  return render(request, 'product_Category/shirts.html', context)

def sweatsPage(request):
  context = {}
  return render(request, 'product_Category/sweats.html', context)

def coatsPage(request):
  context = {}
  return render(request, 'product_Category/coats.html', context)