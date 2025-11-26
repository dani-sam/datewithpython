# students/forms.py
from django import forms
from .models import Student

DEPT_CHOICES = [
    ("BCA", "BCA"),
    ("BSc CS", "BSc Computer Science"),
    ("BCom", "BCom"),
]


class StudentRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput()
    )

    class Meta:
        model = Student
        fields = ["name", "email", "age", "department", "password"]

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your full name"}),
            "email": forms.EmailInput(attrs={"placeholder": "example@mail.com"}),
            "age": forms.NumberInput(attrs={"min": 18}),
            "department": forms.RadioSelect(choices=DEPT_CHOICES),
            "password": forms.PasswordInput(attrs={"placeholder": "Create password"}),
        }

    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 18:
            raise forms.ValidationError("Minimum age must be 18.")
        return age

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("password")
        p2 = cleaned.get("confirm_password")

        if p1 and p2 and p1 != p2:
            self.add_error("confirm_password", "Passwords do not match!")

        return cleaned
