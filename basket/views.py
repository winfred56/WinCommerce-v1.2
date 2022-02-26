from django.shortcuts import get_object_or_404, redirect
from shop.models import Product
from .models import Cart, CartItem
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required()
def add_to_cart(request, slug):
    # Get the product to be added to the cart
    product = get_object_or_404(Product, slug=slug)
    # Get item if it's already in the cart_item or create a cart_item for the product
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user, ordered=False)
    # Filter according to the current logged-in user and incomplete orders
    cart_ = Cart.objects.filter(user=request.user, ordered=False)
    # If there are any incomplete orders for the current logged-in user:
    if cart_.exists():
        cart = cart_[0]
        if cart.products.filter(product__slug=product.slug).exists():
            cart_item.quantity += 1
            cart_item.save()
            messages.info(request, "Product successfully updated in cart")
        else:
            messages.info(request, "Product successfully added to cart")
            cart.products.add(cart_item)
    else:
        ordered_date = timezone.now()
        cart = Cart.objects.create(user=request.user, ordered_date=ordered_date)
        cart.products.add(cart_item)
        messages.info(request, "Product successfully added to cart")
    return redirect("shop:product_detail", slug=slug)


@login_required()
def remove_from_cart(request, slug):
    # Get the product to be added to the cart
    product = get_object_or_404(Product, slug=slug)
    cart_ = Cart.objects.filter(user=request.user, ordered=False)
    if cart_.exists():
        cart = cart_[0]
        if cart.products.filter(product__slug=product.slug).exists():
            cart_item = CartItem.objects.filter(product=product, user=request.user, ordered=False)[0]
            cart.products.remove(cart_item)
            messages.info(request, "Product successfully removed from cart")
            return redirect("shop:product_detail", slug=slug)
        else:
            messages.info(request, "Product not in cart")
            return redirect("shop:product_detail", slug=slug)
    else:
        return redirect("shop:product_detail", slug=slug)

