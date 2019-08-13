from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def item_list(requests):
    context = {
        'items' : ITEM.objects.all()
    }
    return render(requests,'item_list.html',context)