from django.urls import path
from .views import *
app_name= 'shopperapp'
urlpatterns = [
    path('', HomeView.as_view(), name="item_list"),
    path('product/<slug>/', ItemDetailView.as_view(), name="product")

]
