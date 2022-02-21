from django.urls import path
from . import views

app_name = "basket"
urlpatterns = [
    path('add_to_cart/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug:slug>/', views.remove_from_cart, name='remove_from_cart'),
]