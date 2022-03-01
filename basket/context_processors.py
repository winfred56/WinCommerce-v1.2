from .models import Cart

def counter(request):
    cart_ = Cart.objects.filter(user=request.user, ordered=False)
    if cart_.exists():
        cart = cart_[0]
        if cart.products.exists():
            up = cart.products.count()
            return {'count': up}