from django.urls import path
from .views import *

app_name = 'service'
urlpatterns = [
    path('service/', index, name='services')
]
