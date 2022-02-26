from django.shortcuts import render
from .forms import TestimonialForm
from .models import Testimonial

# Create your views here.


def about_view(request):
    form = TestimonialForm()
    template = 'about.html'

    testimonials = Testimonial.objects.filter(approved=True)

    context = {
        'form': form,
        'testimonials': testimonials,
    }

    return render(request, template, context)