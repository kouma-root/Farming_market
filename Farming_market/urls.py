
from django.contrib import admin
from django.urls import path
from Product.views import index, product_detail
from django.conf.urls.static import static
from Farming_market import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("product/<str:slug>/", product_detail, name="product"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
