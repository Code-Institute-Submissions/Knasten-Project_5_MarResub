from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator


from .forms import TestimonialForm, QuestionForm
from .models import Testimonial, Question

# Create your views here.
    

def about_view(request):
    """ Uses form data to add data to DB and also queries testimonials """
    if request.method == "POST":
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.name = request.user
            testimonial.save()
            messages.success(request, 'Testimonial has been submitted for review!')
            return redirect('about')
    form = TestimonialForm()
    template = 'about/about.html'


    testimonials = Testimonial.objects.filter(approved=True)

    paginator = Paginator(testimonials, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    context = {
        'form': form,
        'testimonials': testimonials,
        'page_obj': page_obj
    }

    return render(request, template, context)


def create_question(request):
    """ Creates question from form and saves it """
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save()
            messages.success(request, f'A confirmation email has been sent to your email at {question.email}!')
            return redirect('home')
