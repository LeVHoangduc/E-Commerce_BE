# Generated by Django 4.2 on 2023-05-22 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_remove_product_id_alter_product__id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]