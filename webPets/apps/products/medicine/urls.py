from django.urls import path
from apps.products.medicine.views import addMedicine, listMedicines, editMedicine, deleteMedicine, detailsMedicine

urlpatterns = [
    path('addMedicines/', addMedicine, name="addMedicines"),
    path('listMedicines/', listMedicines, name="listMedicines"),
    path('editMedicine/<int:idMedicine>/', editMedicine, name='editMedicines'),
    path('deleteMedicine/<int:idMedicine>/',
         deleteMedicine, name='deleteMedicine'),
    path('detailsMedicine/<int:idMedicine>/',
         detailsMedicine, name='detailsMedicine'),
]
