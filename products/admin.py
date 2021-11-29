from django.contrib import admin
from .models import Product, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

    
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'category',
        'make',
        'model_id',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
