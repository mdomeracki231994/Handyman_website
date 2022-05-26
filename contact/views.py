from django.shortcuts import render
from .models import CustomerContact


def index(request):
    return render(request, 'contact/index.html')


def thank_you(request):
    if request.POST:
        customer = CustomerContact()
        data = request.POST.dict()
        name = data.get('customer_name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        customer.name = name
        customer.email = email
        customer.subject = subject
        customer.message = message
        customer.save()
    return render(request, 'contact/thank_you.html')
