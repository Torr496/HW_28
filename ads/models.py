from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


class Ad(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=20)
    address = models.CharField(max_length=20)
    is_published = models.BooleanField(default=False)