from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from musicalapp.models import Instrument


class Cart(models.Model):
    insrument=models.ForeignKey(Instrument,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Order(models.Model):
    totaBill=models.IntegerField()
    status=models.CharField(max_length=30,default="processing")
    order_date=models.DateField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)



