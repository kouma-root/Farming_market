from django.shortcuts import render, get_object_or_404
from Product.models import Item

from django.http import HttpResponse

def index(request):
    products = Item.objects.all()
    return render(request, 'product/index.html', context={"products": products})


def product_detail(request, slug):
   product = get_object_or_404(Item, slug=slug)
   return render(request, 'product/detail.html', context={'product': product})
    
    
def search_product(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        products = Item.objects.filter(name__contains= searched)
        return render(request, 'product/search_product.html', context= {'searched': searched, 'products': products})
