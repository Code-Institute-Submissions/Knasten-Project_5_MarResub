from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_cart(request):

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):

    product = Product.objects.get(pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
        messages.success(request, f'Added {product.name} to your cart!')

    request.session['cart'] = cart
    return redirect(redirect_url)


def change_cart(request, product_id):

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[product_id] = quantity
    else:
        cart.pop(product_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, product_id):

    try:
        product = get_object_or_404(Product, pk=product_id)
        cart = request.session.get('cart', {})
        cart.pop(product_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        print(e)
        return HttpResponse(status=500)
