# Generated by Django 4.2 on 2023-05-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_product__id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=10000000000000),
        ),
    ]
