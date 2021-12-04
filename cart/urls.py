from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<product_id>/', views.add_to_cart, name='add_to_cart'),
    path('change/<product_id>/', views.change_cart, name='change_cart'),
    path('remove/<product_id>/', views.remove_from_cart, name='remove_from_cart'),
]