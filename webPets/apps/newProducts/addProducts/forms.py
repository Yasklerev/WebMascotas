from django import forms
from apps.newProducts.addProducts.models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products

        fields = [
            'name_product',
            'type_of_pet',
            'type_of_product',
            'description',
        ]
        labels = {
            'name_product': "Nombre del producto",
            'type_of_pet': "Tipo de mascota",
            'type_of_product': "Tipo de producto",
            'description': "Descripcion",
        }
        widgets = {
            'name_product': forms.TextInput(attrs={'class':'validate'}),
            'type_of_pet': forms.TextInput(attrs={'class':'validate'}),
            'type_of_product': forms.TextInput(attrs={'class':'validate'}),
            'description': forms.TextInput(attrs={'class':'validate'}),
        }