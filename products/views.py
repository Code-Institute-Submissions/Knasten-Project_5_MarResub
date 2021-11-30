from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def all_products(request):

    products = Product.objects.all()
    categories = Category.objects.all()
    query = None  # Needed to make sure it dosent bug, when not entering a seach value.

    if request.GET:
        if 'search_bar' in request.GET:
            query = request.GET['search_bar']
            if not query:
                messages.error(request, "Please enter some keywords to search for!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)


    context = {
        'products': products,
        'categories': categories,
        'search_kw': query,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, id):

    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)