from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def all_products(request):

    products = Product.objects.all()
    categories = Category.objects.all()
    query = None  # Needed to make sure it dosent bug, when not entering a search value.
    sort = None
    sortTwo = None
    direction = None

    if request.GET:
        if 'search_bar' in request.GET:
            query = request.GET['search_bar']
            if not query:
                messages.error(request, "Please enter some keywords to search for!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(sku__contains=query)
            products = products.filter(queries)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'sort' in request.GET:
            sort = request.GET['sort']
            sortTwo = sort

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortTwo = f'-{sort}'
            products = products.order_by(sortTwo)

    selected_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'selected_categories': categories,
        'selected_sorting': selected_sorting,
        'search_kw': query,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, id):

    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)