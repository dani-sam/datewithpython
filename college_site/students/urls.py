# students/urls.py
from django.urls import path
from .views import register_student, success_page

urlpatterns = [
    path("", register_student, name="home"),
    path("register/", register_student, name="register_student"),
    path("success/", success_page, name="success_page"),
]
