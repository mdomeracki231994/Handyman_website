from django.core.paginator import Paginator
from django.shortcuts import render
from services.models import Services

# TODO  ad

def index(request):
    services = Services.objects.all()
    return render(request, 'services/index.html', {'services': services})
