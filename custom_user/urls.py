from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

urlpatterns = [
    path("register/",user_register,name="user_register"),
    path("login/",user_login,name="user_login"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

