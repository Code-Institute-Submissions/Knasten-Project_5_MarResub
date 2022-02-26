from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):

    class Meta:
        model = Testimonial
        fields = ('rating', 'content',)

        name = forms.CharField,
        rating = forms.IntegerField,
        content = forms.Textarea

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
