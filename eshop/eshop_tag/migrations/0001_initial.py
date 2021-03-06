# Generated by Django 3.2.8 on 2021-10-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eshop_products', '0003_auto_20211025_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('activa', models.BooleanField(default=True)),
                ('products', models.ManyToManyField(blank=True, to='eshop_products.Product')),
            ],
        ),
    ]
