from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import *
from django.views.generic import ListView, DetailView
# Create your views here.
from django.utils import timezone



def products(request):
    context = {
        'items': ITEM.objects.all()
    }
    return render(request, 'product-page.html', context)

def checkout(request):
    return render(request,"checkout-page.html")


class HomeView(ListView):
    model = ITEM
    template_name = "home-page.html"

class ItemDetailView(DetailView):
    model = ITEM
    template_name = "product-page.html"

def add_to_cart(request,slug):
    item = get_object_or_404(ITEM,slug=slug)
    order_item,created = ORDER_ITEM.objects.get_or_create(item=item,
                                                  user=request.user,
                                                  ordered=False)
    order_qs = ORDER.objects.filter(user=request.user,ordered = False)
    if order_qs.exists():
        order  = order_qs[0]
        #check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
    else:
        ordered_date = timezone.now()
        order = ORDER.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)

    return redirect("shopperapp:product",slug=slug)