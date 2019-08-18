from django.shortcuts import render,HttpResponse
from .models import *
from django.views.generic import ListView, DetailView
# Create your views here.




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
