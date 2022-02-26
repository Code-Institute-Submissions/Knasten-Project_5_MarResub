from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import TestimonialForm
from .models import Testimonial

# Create your views here.
    

def about_view(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.name = request.user
            testimonial.save()
            messages.success(request, 'Testimonial has been submitted for review!')
            return redirect('about')
    form = TestimonialForm()
    template = 'about.html'

    testimonials = Testimonial.objects.filter(approved=True)

    context = {
        'form': form,
        'testimonials': testimonials,
    }

    return render(request, template, context)