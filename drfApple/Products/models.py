import uuid
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    # _id = models.IntegerField(default=0)
    _id = models.AutoField(primary_key=True)
    # _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    rating = models.FloatField()
    price_before_discount = models.IntegerField()
    quantity = models.IntegerField()
    sold = models.IntegerField()
    view = models.IntegerField()
    name = models.CharField(max_length=255)
    image = models.URLField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    description = models.CharField(default="", max_length=10000000000000)

    def __str__(self):
        return self.name
