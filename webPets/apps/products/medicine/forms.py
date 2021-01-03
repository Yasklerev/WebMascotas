from django import forms
from apps.products.medicine.models import Medicine


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine

        fields = [
            'name_medicine',
            'resume',
            'description',
            'type_of_pet',
            'type_of_medicine',
            'amount_dose',
            'medicine_cost',
        ]
        labels = {
            'name_medicine': 'Nombre de la medicina',
            'resume': 'Resumen medicina',
            'description': 'Descripción medicina',
            'type_of_pet': 'Tipo de mascota',
            'type_of_medicine': 'Tipo de medicina',
            'amount_dose': 'Cantidad de dosis',
            'medicine_cost': 'Valor de la medicina'
        }
        widgets = {
            'name_medicine': forms.TextInput(attrs={'class': 'validate'}),
            'resume': forms.TextInput(attrs={'class': 'validate'}),
            'description': forms.TextInput(attrs={'class': 'validate'}),
            'type_of_pet': forms.TextInput(attrs={'class': 'validate'}),
            'type_of_medicine': forms.TextInput(attrs={'class': 'validate'}),
            'amount_dose': forms.NumberInput(attrs={'class': 'validate'}),
            'medicine_cost': forms.NumberInput(attrs={'class': 'validate'}),
        }
