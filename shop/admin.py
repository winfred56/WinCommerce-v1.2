from django.contrib import admin
from .models import Product, Category, A_image, A_color, A_size

admin.site.register(A_image)
admin.site.register(A_color)
admin.site.register(A_size)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'discount_price', 'price', 'category', 'seller', 'in_stock', 'slug','brand','display_image',
                    'created', 'updated']
    list_editable = ['discount_price', 'price', 'in_stock']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'slug']
    prepopulated_fields = {'slug': ('category',)}

