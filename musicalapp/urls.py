from django.urls import path
from musicalapp import views
urlpatterns = [
    path('',views.index,name='home'),
]
