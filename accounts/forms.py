from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class SignUpForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User

        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )



class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = [
            "full_name",
            "phone_number",
            "bio"
        ]

        widgets = {

            "full_name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5
                }
            ),

        }