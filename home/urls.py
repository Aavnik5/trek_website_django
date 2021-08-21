
from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('choose-treck',choosetreck, name='choosetreck'),
    path('trecks',treck, name='treck'),
    path('Contact-us',contactus, name='contactus'),
    path('About-us',aboutus, name='aboutus'),
    path('Book-treck',booktreck, name='booktreck'),

]
