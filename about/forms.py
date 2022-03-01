from django import forms
from .models import Testimonial, Question


class TestimonialForm(forms.ModelForm):

    class Meta:
        model = Testimonial
        fields = ('rating', 'content')

        rating = forms.IntegerField,
        content = forms.Textarea

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'

        name = forms.CharField,
        email = forms.EmailField,
        title = forms.CharField,
        question = forms.Textarea,
        telephone = forms.CharField,

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
