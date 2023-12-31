# Generated by Django 4.2.2 on 2023-06-22 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0007_alter_review_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('delivery_type', models.CharField(default='', max_length=30)),
                ('payment_type', models.CharField(default='', max_length=30)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('status', models.CharField(default='', max_length=30)),
                ('city', models.CharField(default='', max_length=30)),
                ('address', models.CharField(default='', max_length=100)),
                ('products', models.ManyToManyField(related_name='products', to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
