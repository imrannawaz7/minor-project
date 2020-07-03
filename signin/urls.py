from django.urls import path
# from .views import UserApiView
from . import views

urlpatterns = [
    path('signin/', views.login, name = "signin"),
    path('submit/', views.signinUser, name="signinb"),
]