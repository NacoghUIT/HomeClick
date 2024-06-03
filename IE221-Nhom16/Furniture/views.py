from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse 
from .models import *
import json
from django.contrib.auth import authenticate
from django.contrib import messages
import logging
from django.shortcuts import render
from django.db.models import Q



# Create your views here.
def home(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        messages.success(request, 'Đã thêm vào giỏ hàng')
        cartItems = order.get_cart_items
    else:
        items = []
        order  = {'get_cart_items': 0,'get_cart_total': 0}
        cartItems = order['get_cart_items']
    context = {'items':items, 'order': order}
    products = Product.objects.all()
    context = {'products':products,'cartItems':cartItems}
    return render(request, 'app/home.html',context)

def product(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        messages.success(request, 'Đã thêm vào giỏ hàng')
    else:
        items = []
        order  = {'get_cart_items': 0,'get_cart_total': 0}
        cartItems = order['get_cart_items']
    context = {'items':items, 'order': order}
    products = Product.objects.all()
    context = {'products':products,'cartItems':cartItems}
    return render(request,"app/product.html",context)
    
def cart(request):
    # Kiểm tra
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order  = {'get_cart_items': 0,'get_cart_total': 0}
        cartItems = order['get_cart_items']
    context = {'items':items, 'order': order, 'cartItems': cartItems}
    return render(request,"app/cart.html",context)

def checkout(request):
    # Kiểm tra
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order  = {'get_cart_items': 0,'get_cart_total': 0}
        cartItems = order['get_cart_items']
    context = {'items':items, 'order': order,'cartItems': cartItems}
    return render(request,"app/checkout.html",context)



def updateItem(request):
    data = json.loads(request.body)
    # Lấy từ data
    productId = data['productId']
    action = data['action']
    product = Product.objects.get(id = productId)
    
    # User order gì thì lấy lại
    order, created = Order.objects.get_or_create(customer = customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)
    
    # Thêm hành động
    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    
    
    return JsonResponse('added', safe = False)

def detail(request):
    context = {}
    return render(request,"app/detail.html",context)

# Search
def searchpage(request):
    context = {}
    if request.method == "POST":
        searched = request.POST['searched']
        product = Product.objects.filter(Q(name__contains=searched) | Q(code__contains=searched))
        
        return render(request, "app/searchpage.html", {'searched': searched, 'product': product})
    else:
        return render(request, "app/searchpage.html", context)
