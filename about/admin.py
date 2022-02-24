from django.contrib import admin
from .models import Testimonial

# Register your models here.

class TestimonialAdmin(admin.ModelAdmin):

    ordering = ('-created_on', )

admin.site.register(Testimonial, TestimonialAdmin)