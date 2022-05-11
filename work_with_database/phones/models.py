from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.TextField(max_length=50)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.TextField(max_length=50)
