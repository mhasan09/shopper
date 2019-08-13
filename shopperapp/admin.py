from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ITEM)
admin.site.register(ORDER_ITEM)
admin.site.register(ORDER)