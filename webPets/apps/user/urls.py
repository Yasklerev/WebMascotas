from django.conf.urls import url
from django.urls import path
from apps.user.views import RegisterUser

urlpatterns = [
    path('newUser/', RegisterUser.as_view(), name="registerUser"),
]

# GHfs487hG  Manuel

# JDHGS659ik  Rodrigo

# HBSY655Khb Jose

# HBSY655Khb Maria

# natalia
