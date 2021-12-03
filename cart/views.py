from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    
    return render(request, 'cart/cart.html')

def add_to_cart(request, product_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity


    request.session['cart'] = cart
    return redirect(redirect_url)