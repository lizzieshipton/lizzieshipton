from django.shortcuts import render
from models import Item

def index(request):
    items = Item.objects.order_by("name")
    return render(request, 'index.html', {"items": items})
