from django.urls import path
from apps.userMenu.paymentHistory.views import index
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('paymentHistory/', login_required(index))
]
