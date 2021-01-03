from django.urls import path
from apps.userMenu.shoppingCart.views import index
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('shoppingCart/', login_required(index))
]
