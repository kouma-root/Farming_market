from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from Users.decorators import farmer_required, buyer_required
from Product.models import Item
from .models import Request
from .forms import RequestForm

@login_required
@buyer_required
def create_request_buyers(request, product_id):
    product = get_object_or_404(Item, id = product_id)
    
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.buyer = request.user
            req.product = product
            req.save()
            
            return redirect("buyer_dashboard")
    else:
        form = RequestForm()
        
    return render(request, 'request/create_request.html', context= {'form': form, 'product': product})



@login_required
@farmer_required
def farmers_request_view(request):
    
    products = Item.objects.filter(owner= request.user)
    request_list = Request.objects.filter(product__in = products)
    
    return render(request, 'request/farmer_requests.html', context= {'requests': request_list})


@login_required
@farmer_required
def update_request_status(request, request_id, status):
    
    req = get_object_or_404(Request, id = request_id, product__farmer= request.user)
    
    if status in ["Approved", "Rejected"]:
        req.status = status
        req.save()
        
    return redirect('farmer_requests')


@login_required
@buyer_required
def buyer_requests_list(request):
    requests = Request.objects.filter(buyers=request.user)
    return render(request, 'request/buyer_requests.html', {'requests': requests})