from django.db import models

# Create your models here.


class Medicine(models.Model):
    name_medicine = models.CharField(max_length=50)  # Nombre medicina
    resume = models.CharField(max_length=50)  # Resumen medicina
    description = models.CharField(max_length=50)  # Descripción de la medicina    
    type_of_pet = models.CharField(max_length=50) # Tipo de mascota a quien va dirigida la medicina.
    type_of_medicine = models.CharField(max_length=50)  # Tipo de medicina
    amount_dose = models.CharField(max_length=50)  # Cantidad de dosis
    medicine_cost = models.IntegerField(default=0) # Valor de la medicina
