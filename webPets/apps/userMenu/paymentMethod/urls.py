from django.urls import path
from apps.userMenu.paymentMethod.views import index
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('paymentMethod/', login_required(index))
]
