from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
   # return HttpResponse("HELLO DJANGO WORLD")
   return render(request,'sample.html',{'name':'mahendra'})


def sum(request):
   a=int(request.POST['no1'])
   b=int(request.POST['no2'])
   ans=a+b
   return render(request,'result.html',{'result':ans})   