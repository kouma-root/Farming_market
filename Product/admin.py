from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'slug', 'cathegory', 'quantity', 'price',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Item, ItemAdmin)