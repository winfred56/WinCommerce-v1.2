from django.db import models
from django.conf import settings
from shop.models import Product
from accounts.models import UserBase


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField('CartItem')
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user.user_name

    def get_order_total(self):
        total = 0
        for item in self.products.all():
            total = total + item.get_total_price()
        return total


class CartItem(models.Model):
    user = models.ForeignKey(UserBase, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    def get_total_price(self):
        item_price = self.product.price
        item_quantity = self.quantity
        total = item_price * item_quantity
        return total

    def get_total_discount_price(self):
        item_price = self.product.discount_price
        item_quantity = self.quantity
        total = item_price * item_quantity
        return total