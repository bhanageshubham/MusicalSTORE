

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from cartapp.models import Cart, Order
from musicalapp.models import Instrument


def addtocart(request, id):
   c=Cart()
   instrumentid=Instrument.objects.get(id=id)
   uid=request.session.get('uid')
   userid=User.objects.get(id=uid)
   c.insrument=instrumentid
   c.user=userid
   c.save()
   messages.info(request,"Cart Added successfully")
   return redirect("/")


def cartlist(request):
   uid=request.session.get('uid')
   cr=Cart.objects.filter(user=uid)
   if request.method=="POST":
     totalbill=0
     qty=int(request.POST['qty'])
     for i in cr:
        totalbill=totalbill+i.insrument.price *qty
     o=Order()
     o.totaBill=totalbill
     o.user=User.objects.get(id=uid)
     o.status='completed'
     o.save()
     for i in cr:
        i.delete()
     return render(request,'index.html',{'totalbill':totalbill})

   else:

     d={'cr':cr}
     return render(request,"cartlist.html",d)

