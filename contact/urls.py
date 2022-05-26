from django.urls import path
from .views import *

app_name = 'contact'
urlpatterns = [
    path('', index, name='contact'),
    path('thankyou/', thank_you, name='thank_you_page')
]
