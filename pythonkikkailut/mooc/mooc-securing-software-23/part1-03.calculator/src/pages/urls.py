from django.urls import path

from .views import homePageView
from .views import addView 
from .views import multiplyView 

urlpatterns = [

    path('', homePageView, name='home'),
    path('add/', addView, name='add'),
    path('multiply/', multiplyView, name='multiply')
]
