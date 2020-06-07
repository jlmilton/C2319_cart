from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse
from .models import About
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import (
Item, Order, OrderItem
)
# Create your views here.
def home(request):
    return render(request, '../templates/home.html', {'title': 'Home'})

def about(request):
    return render(request, '../templates/about.html', {'title': 'About'})

def milestone_17(request):
    return render(request, '../templates/milestone_17.html', {'title': 'Milestone 17'})

def forsale(request):
    return render(request, '../templates/forsale.html', {'title': 'For Sale'})

class HomeView(ListView):
    model= Item
    template_name = "home.html"

class ProductView(DetailView):
    model = Item
    template_name = "product.html"

def add_to_cart(request, pk):
    item = get_object_or_404(Item,pk = pk)
    order_item,created= OrderItem.objects.get_or_create(item= item, user=request.user, ordered = False)
    order_qs = Order.objects.filter(user = request.user, ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Added Quantity Item!")
            return redirect("home:product", pk = pk)
        else:
            order.items.add(order_item)
            messages.info(request,"ITem added to your cart")
            return redirect("home:product",pk=pk)
    else:
        ordered_date=timezone.now()
        order=Order.objects.create(user=request.user,order_date=order_date)
        order.items.add(order_item)
        messages.info(request,"items added to your cart")
        return redirect("home:product",pk=pk)

def remove_from_cart(request,pk):
    item = get_object_or_404(Item, px=pk)
    order_qs=Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        if order.items.filter(item__pk= item.pk).exists():
            order_item=OrderItem.objects.filter(item=item,user=request.user,ordered=False)[0]
            order_item.delete()
            messages.info(request,"Item \""+ order_item.item.item_name+"\"removed from your cart")
            return redirect("home:product")
        else:
            messages.info(request,"this item not in your cart")
            return redirect("home:product",pk=pk)
    else:
        messages.info(request,"you do not have an order")
        return redirect("home:product",pk=pk)

