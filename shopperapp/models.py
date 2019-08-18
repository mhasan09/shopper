from django.db import models
from django.conf import settings
from django.shortcuts import reverse
# Create your models here.
CATEGORY_CHOICES = (('S','Shirt'),('SW','Sport wear'),('OW','Outwear'))
LABEL_CHOICES = (('P','Primary'),('S','Secondary'),('D','Danger'))

class ITEM(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True,null=True)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    label = models.CharField(choices=LABEL_CHOICES,max_length=2)
    slug = models.SlugField()
    description = models.TextField()
    def __str__(self):
        return self.title
    def get_absoulute_url(self):
        return reverse("shopperapp:product",kwargs={
            'slug':self.slug
        })
    def get_to_cart_url(self):
        return reverse("shopperapp:add-to-cart", kwargs={
            'slug': self.slug
        })


class ORDER_ITEM(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default= False)
    item = models.ForeignKey(ITEM,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

class ORDER(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items = models.ManyToManyField(ORDER_ITEM)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default= False)

    def __str__(self):
        return self.user.username