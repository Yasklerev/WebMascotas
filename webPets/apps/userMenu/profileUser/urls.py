from django.urls import path
from apps.userMenu.profileUser.views import index
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('userPerfil/', login_required(index)),
]
