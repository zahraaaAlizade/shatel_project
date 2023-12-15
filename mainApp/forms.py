from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "national_id", "email", "password")
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.national_id = self.cleaned_data['national_id']

        if commit:
            user.save()
        return user


