from django.contrib import admin
from .models import Product, Category, Review

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


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'product',
        'title',
        'review',
        'created_on',
        'approved',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
