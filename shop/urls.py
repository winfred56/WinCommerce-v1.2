from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.categories_list, name='category_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
]