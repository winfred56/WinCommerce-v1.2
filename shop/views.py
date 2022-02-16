from django.shortcuts import render
from .models import Product, Category


def categories(request):
    return {'cat': Category.objects.all()}


def home(request):
    products = Product.objects.all()
    search = request.GET.get('search')
    if search != " " and search is not None:
        products = Product.objects.filter(name__icontains=search)
    context = {'products': products}
    return render(request, 'shop/home.html', context)


def categories_list(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'shop/category.html', context)


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'shop/detail.html', context={'product': product})
