from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import ProfileForm

from checkout.models import Order

import datetime

# Create your views here.

def profile(request):
    """ Displays the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated!")
        else:
            messages.error(request, 'Something went wrong, please try again!')

    form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    for order in orders:
        date = order.date.strftime('%d/%m/%Y')


    template = 'profiles/profile.html'
    context = {
        'orders': orders,
        'form': form,
        'on_profile_page': True,
        'date': date,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'Order confirmation for order {order_number}.\
            This order was created on {order.date}'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, template, context)