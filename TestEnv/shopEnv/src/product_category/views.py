from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime

# from .models import Product
# import all model(s)
from .models import *

# Create your views here.
def basePage(request):
  context = {}
  return render(request, 'product_category/base.html', context)

# Homepage view
def homePage(request):
  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

  else:
    items = [] 
    order = {'get_cart_total': 0, 'get_cart_items':0, 'shipping':False}
    cartItems = order['get_cart_items']

  context = {'cartItems': cartItems}
  return render(request, 'product_category/home.html', context)

# Jeans view
def jeansPage(request):

  obj = Product.objects.filter(category='jeans')

  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
  else:
    items = [] 
    order = {'get_cart_total': 0, 'get_cart_items':0,  'shipping':False}
    cartItems = order['get_cart_items']

  context = {'object': obj, 'items': items, 'order': order, 'cartItems': cartItems}
  return render(request, 'product_category/jeans.html', context)

# Shirts view
def shirtsPage(request):
  obj = Product.objects.filter(category='shirts')

  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
  else:
    items = [] 
    order = {'get_cart_total': 0, 'get_cart_items':0, 'shipping':False}
    cartItems = order['get_cart_items']

  context = {'object': obj, 'items': items, 'order': order, 'cartItems': cartItems}
  return render(request, 'product_category/shirts.html', context)

# Sweats views
def sweatsPage(request):
  queryset = Product.objects.filter(category='sweats')


  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
  else:
    items = [] 
    order = {'get_cart_total': 0, 'get_cart_items':0, 'shipping':False}
    cartItems = order['get_cart_items']

  context = {'object_list': queryset, 'items': items, 'order': order, 'cartItems': cartItems}
  return render(request, 'product_category/sweats.html', context)

# Coats view
def coatsPage(request):
  obj = Product.objects.filter(category='coats')


  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
  else:
    items = [] 
    order = {'get_cart_total': 0, 'get_cart_items':0, 'shipping':False}
    cartItems = order['get_cart_items']

  context = {'object': obj, 'items': items, 'order': order, 'cartItems': cartItems}
  return render(request, 'product_category/coats.html', context)

# Productdetail view
def product_details(request, id):
  obj = Product.objects.get(id=id)


  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
  else:
    items = [] 
    order = {'get_cart_total': 0, 'get_cart_items':0, 'shipping':False}
    cartItems = order['get_cart_items']

  context = {'object': obj, 'cartItems': cartItems}
  return render(request, 'product_category/product_details.html', context)

# Cartpage view
def cartPage(request):
  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

  else:
    items = [] 
    order = {'get_cart_total': 0, 'get_cart_items':0, 'shipping':False}
    cartItems = order['get_cart_items']

  context = {'items': items, 'order': order, 'cartItems': cartItems}
  return render(request, 'product_category/cart.html', context)

# Checkoutpage view
def checkoutPage(request):
  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

  else:
    items = [] 
    order = {'get_cart_total': 0, 'get_cart_items':0, 'shipping':False}
    cartItems = order['get_cart_items']

  context = {'items': items, 'order': order, 'cartItems': cartItems}
  return render(request, 'product_category/checkout.html', context)

# For rendering a HTTP response
def updateItem(request):
  data = json.loads(request.body) # from the body attribute specified in myscrip.js
  productID = data['productID']
  action = data['action']

  print('Action:', action)
  print('ProductID:', productID)

  # to avoid the problem with RelatedObjectDoesNotExist exception
  try:
    customer = request.user.customer
  except Customer.DoesNotExist:
    customer = Customer.objects.create(user=request.user)

  customer = request.user.customer
  product = Product.objects.get(id=productID)
  print("Name of product is: ", product.name)
  print("Price of product is: ", product.price)
  order, created = Order.objects.get_or_create(customer=customer, complete=False)
  orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

  print("Order quantity before is: ", orderItem.quantity)

  if action == 'add':
    orderItem.quantity = (orderItem.quantity + 1)
  elif action == 'remove':
    orderItem.quantity = (orderItem.quantity - 1)

  orderItem.save()
  print("Order quantity after is: ", orderItem.quantity)

  if orderItem.quantity <= 0:
    orderItem.delete()
  return JsonResponse('Item was added', safe=False)

def processOrder(request):
  print('Data:', request.body)
  transaction_id = datetime.datetime.now().timestamp()
  data = json.loads(request.body)

  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    # verifying if the front end total is the same as value on the backend
    # to prevent theft 
    if total == order.get_cart_total:
      order.complete = True
    
    order.save()

    if order.shipping == True:
      ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
      )

  else:
    print('User is not logged in...')
  return JsonResponse('Payment completed', safe=False)