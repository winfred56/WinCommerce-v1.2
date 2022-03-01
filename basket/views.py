from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from shop.models import Product
from .models import Cart, CartItem


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
            print(cart.products.count())
            messages.info(request, "Product successfully updated in cart")
            return redirect("basket:cart")
        else:
            messages.info(request, "Product successfully added to cart")
            cart.products.add(cart_item)
    else:
        ordered_date = timezone.now()
        cart = Cart.objects.create(user=request.user, ordered_date=ordered_date)
        cart.products.add(cart_item)
        messages.info(request, "Product successfully added to cart")
    return redirect("basket:cart")



# get cartItem for specific user
# get cart for the specific user
# we make sure cartItem exits in users cart
# we make sure cartItem isn't ordered
# we remove cartItem from cart

@login_required()
def remove_cart_item(request, slug):
    # gets cart_item
    _cart_item_to_remove = get_object_or_404(CartItem, product__slug=slug)

    # gets cart for specific user
    _cart = Cart.objects.filter(user=request.user, ordered=False, products__ordered=False)

    if _cart.exists():

        # gets the most recent cart queryset
        recent_cart = _cart[0]
      # removes cart_item from recent cart
        recent_cart.products.remove(_cart_item_to_remove)

        # deletes cart_item

        CartItem.delete(_cart_item_to_remove)

        # deletes cart if no cart_item exits
        if recent_cart.products.count() == 0:
            Cart.delete(recent_cart)

        return redirect('/')
    return HttpResponse('Hello world!')


@login_required
def cart(request):
    basket = CartItem.objects.all().filter(user=request.user, ordered=False)

    context = {'basket': basket}
    return render(request, 'shop/cart.html', context)