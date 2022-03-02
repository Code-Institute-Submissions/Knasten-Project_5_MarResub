from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm

# Create your views here.


def all_products(request):
    """View returns all products and sorts/filters"""
    products = Product.objects.all()
    categories = Category.objects.all()
    query = None  # Needed to make sure it dosent bug, when not entering a search value.
    sort = None
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
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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

    form = ReviewForm()
    review_list = Review.objects.filter(product=id, approved=True)
    paginator = Paginator(review_list, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'product': product,
        'form': form,
        'page_obj': page_obj,
    }

    return render(request, 'products/product_detail.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='home')
def add_product(request):
    """View for superusers to add products"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product was added successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Something went wrong! Please check the form and try again')
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@user_passes_test(lambda u: u.is_superuser, login_url='home')
def edit_product(request, product_id):
    """View to edit product"""
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product was edited successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Something went wrong! Please check the form and try again')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Currently editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@user_passes_test(lambda u: u.is_superuser, login_url='home')
def delete_product(request, product_id):
    """View to delete product"""
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product was successfully deleted')
    return(redirect(reverse('products')))


@login_required
def create_review(request, id):
    if request.method == "POST":
        review = Review()
        review.author = request.user
        review.title = request.POST.get('title')
        review.review = request.POST.get('review')
        review.product = get_object_or_404(Product, pk=id)
        review.save()
        messages.success(request, 'Your review is pending approval!')
        return redirect(request.META['HTTP_REFERER'])
    else:
        success_url = "/".join(request.get_full_path().split('/')[:-1])
        return redirect(success_url)