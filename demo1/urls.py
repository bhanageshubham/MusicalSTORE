from django.urls import path

from demo1 import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.sum,name='sum')
]
