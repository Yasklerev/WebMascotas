from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.products.medicine.forms import MedicineForm
from apps.products.medicine.models import Medicine

# Create your views here.


def addMedicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listMedicines')
    else:
        form = MedicineForm()
    return render(request, 'products/medicine//medicineForm.html', {'form': form})


def listMedicines(request):
    medicine = Medicine.objects.all().order_by('id')
    context = {'medicine': medicine}
    return render(request, 'products/medicine//listMedicines.html', context)


def editMedicine(request, idMedicine):
    medicine = Medicine.objects.get(id=idMedicine)
    if request.method == 'GET':
        form = MedicineForm(instance=medicine)
    else:
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
        return redirect('/listMedicines')
    return render(request, 'products/medicine//medicineForm.html', {'form': form})


def deleteMedicine(request, idMedicine):
    medicine = Medicine.objects.get(id=idMedicine)
    if request.method == 'POST':
        medicine.delete()
        return redirect('/listMedicines')
    return render(request, 'products/medicine//deleteMedicine.html', {'medicine': medicine})


def detailsMedicine(request, idMedicine):
    medicine = Medicine.objects.get(id=idMedicine)
    return render(request, 'products/medicine//detailsMedicine.html', {'medicine': medicine})
