
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Farming_market import settings
from Product.views import index, product_detail
from Users.views import register_view, login_view, logout_view, allUsers_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("product/<str:slug>/", product_detail, name="product"),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('all_users', allUsers_view, name='allUsers'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
