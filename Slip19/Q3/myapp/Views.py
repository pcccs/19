from django.shortcuts import render
from .models import Item

def item_list(request):
    items = Item.objects.all()
    return render(request, 'myapp/item_list.html', {'items': items})

def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'myapp/item_detail.html', {'item': item})
