# students/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.register_student, name="register_student"),
    path("register/", views.register_student, name="register_student"),
    path(
        "success/<int:student_id>/",
        views.registration_success,
        name="registration_success",
    ),
]
