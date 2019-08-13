from django.db import models
from django.conf import settings
# Create your models here.
class ITEM(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.title

class ORDER_ITEM(models.Model):
    item = models.ForeignKey(ITEM,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ORDER(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items = models.ManyToManyField(ORDER_ITEM)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default= False)

    def __str__(self):
        return self.user.username