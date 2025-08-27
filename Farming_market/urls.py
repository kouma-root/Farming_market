
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Farming_market import settings
from Product.views import index, product_detail, search_product, add_product, edit_product, delete_product
from Users.views import register_view, login_view, logout_view, all_users_view, farmer_dashboard, buyer_dashboard
from Request.views import create_request_buyers, update_request_status, farmers_request_view, buyer_requests_list, cancel_request, delete_request



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("product/<str:slug>/", product_detail, name="product"),
    path('add_product/', add_product, name='add_product'),
    path("product/<int:item_id>/edit_product/", edit_product, name="edit_product"),
    path("product/<int:item_id>/delete_product/", delete_product, name="delete_product"),
    path('search_product/', search_product, name='search_product'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('allUsers', all_users_view, name='allUsers'),
    path('create/<int:product_id>/', create_request_buyers, name='create_request'),
    path('farmer/', farmers_request_view, name='farmer_requests'),
    path('buyer/', buyer_requests_list, name='buyer_requests'),
    path('update/<int:request_id>/<str:status>/', update_request_status, name='update_request_status'),
    path('cancel/<int:request_id>/', cancel_request, name='cancel_request'),
    path('delete/<int:request_id>/', delete_request, name='delete_request'),
    path('farmer/dashboard/', farmer_dashboard, name='farmer_dashboard'),
    path('buyer/dashboard/', buyer_dashboard, name='buyer_dashboard'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
