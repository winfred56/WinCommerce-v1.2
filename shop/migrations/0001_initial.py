# Generated by Django 4.0.2 on 2022-02-16 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Grocery', 'Grocery'), ('Phones & Tablets', 'Phones & Tablets'), ('Health & Beauty', 'Health & Beauty'), ('Home & Office', 'Home & Office'), ('Electronics', 'Electronics'), ('Computing', 'Computing'), ('Fashion', 'Fashion'), ('Sports & Sporting Goods', 'Sports & Sporting Goods'), ('Baby Products', 'Baby & Products'), ('Automobiles', 'Automobile'), ('Books', 'Books'), ('Movies', 'Movies'), ('Music', 'Music'), ('Toys & Games', 'Toys & Games'), ('Garden & Outdoors', 'Garden & Outdoors'), ('Miscellaneous', 'Miscellaneous'), ('Pet Supplies', 'Pet & Supplies'), ('Livestock', 'Livestock'), ('Industrial & Scientific', 'Industrial & Scientific')], max_length=100)),
                ('slug', models.SlugField(max_length=355, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('brand', models.CharField(max_length=100)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('display_image', models.ImageField(upload_to='display_images/')),
                ('slug', models.SlugField(max_length=355, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('in_stock', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Products',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='A_size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='A_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='other_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='A_color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
