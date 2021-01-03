from django.db import models

# Create your models here.


class Products(models.Model):
    name_product = models.CharField(max_length=50)
    type_of_pet = models.CharField(max_length=50)
    type_of_product = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
