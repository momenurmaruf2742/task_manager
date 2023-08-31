from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Task


class UserLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        help_text="Remember me",
    )

class UserRegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True, help_text='Required. Enter your full name.')

    class Meta:
        model = User
        fields = ['username', 'full_name', 'password1', 'password2']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']
