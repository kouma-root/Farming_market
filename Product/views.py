from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from Users.decorators import farmer_required
from .models import Item
from .forms import ItemForm


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
    else:
        return redirect('index')
    
@login_required
@farmer_required
def add_product(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES) 
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user   
            item.save()
            return redirect("index")  
    else:
        form = ItemForm()

    return render(request, "product/add_product.html", {"form": form})


@login_required
@farmer_required
def edit_product(request, item_id):
    item = get_object_or_404(Item, id=item_id, owner=request.user)
    
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("product", slug=item.slug)
    else:
        form = ItemForm(instance=item)
    return render(request, "product/edit_product.html", {"form": form, "item": item})


@login_required
@farmer_required
def delete_product(request, item_id):
    item = get_object_or_404(Item, id=item_id, owner=request.user)
    if request.method == "POST":
        item.delete()
        return redirect("index")
    return render(request, "product/delete_product.html", {"item": item})