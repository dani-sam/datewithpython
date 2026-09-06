from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from .models import Student


def register_student(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            # Save the student to database
            student = form.save()

            # Redirect to success page with student ID
            return redirect("registration_success", student_id=student.id)
    else:
        form = StudentRegistrationForm()

    # Updated template path to match your structure
    return render(request, "students/register.html", {"form": form})


def registration_success(request, student_id):
    try:
        # Retrieve the student data from database
        student = Student.objects.get(id=student_id)

        context = {"student": student}

        # Updated template path to match your structure
        return render(request, "students/success.html", context)
    except Student.DoesNotExist:
        return redirect("register_student")
