from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login),
    path("logform", views.logform),
    path("reg", views.reg),
    path("regForm", views.regForm),
     path("resume", views.resume),
]