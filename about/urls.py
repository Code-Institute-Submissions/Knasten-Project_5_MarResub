from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_view, name='about'),
    path('create_question', views.create_question, name='create_question'),
]
