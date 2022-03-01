from django.contrib.auth.decorators import login_required

from .models import Cart


def counter(request):
    if request.user.is_authenticated:
        user_cart = Cart.objects.filter(user=request.user, ordered=False, products__ordered=False)
        cart_products_counter = user_cart.count()
        return {'products_counter': cart_products_counter}
    return {'products_counter': 0}