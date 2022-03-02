from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


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
            _send_email_owner(question)
            _send_email_user(question)
            messages.success(request, f'A confirmation email has been sent to your email at {question.email}!')
            return redirect('home')


def _send_email_owner(question):
    """Send confirmation email to owner"""
    template_subject = 'about/confirmation_emails/confirmation_email_subject.txt'
    template_body = 'about/confirmation_emails/confirmation_email_body.txt'
    owner_email = settings.DEFAULT_FROM_EMAIL
    user_email = question.email
    subject = render_to_string(template_subject, {'question': question})
    body = render_to_string(template_body, {'question': question})
    send_mail(subject, body, owner_email, [owner_email])


def _send_email_user(question):
    """Send confirmation email to customer"""
    template_subject = 'about/confirmation_emails/confirmation_email_subject_customer.txt'
    template_body = 'about/confirmation_emails/confirmation_email_body_customer.txt'
    owner_email = settings.DEFAULT_FROM_EMAIL
    user_email = question.email
    subject = render_to_string(template_subject, {'question': question})
    body = render_to_string(template_body, {'question': question})
    send_mail(subject, body, owner_email, [user_email])