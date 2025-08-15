from django.shortcuts import render
from Product.models import Item
from django.http import HttpResponse

def index(request):
    products = Item.objects.all()
    
    return render(request, 'product/index.html', context={"products": products})


def product_detail(request, slug):
    return HttpResponse(slug)