from django.shortcuts import render, redirect

# Create your views here.
from .forms import StudentRegistrationForm


def register_student(request):
    if request.method == "GET":
        form = StudentRegistrationForm()
        return render(request, "students/register.html", {"form": form})

    elif request.method == "POST":
        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            form.save()  # saves Student to DB
            return redirect("success_page")

        return render(request, "students/register.html", {"form": form})


def success_page(request):
    return render(request, "students/success.html")
