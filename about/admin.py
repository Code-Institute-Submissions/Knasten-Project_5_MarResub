from django.contrib import admin
from .models import Testimonial, Question

# Register your models here.

class TestimonialAdmin(admin.ModelAdmin):

    ordering = ('-created_on', )

class QuestionAdmin(admin.ModelAdmin):

    ordering = ('-created_on', )

admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Question, QuestionAdmin)