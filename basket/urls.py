from django.urls import path
from . import views

app_name = "basket"
urlpatterns = [
    path('add_to_cart/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove_cart_item/<slug:slug>/', views.remove_cart_item, name='remove_cart_item'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

]