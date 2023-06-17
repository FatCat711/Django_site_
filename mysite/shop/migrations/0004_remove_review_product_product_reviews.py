# Generated by Django 4.2.2 on 2023-06-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_specification_tag_review_productimage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='reviews',
            field=models.ManyToManyField(related_name='products', to='shop.review'),
        ),
    ]
