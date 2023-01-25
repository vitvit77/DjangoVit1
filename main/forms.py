from .models import Vacancy, Comments
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, NumberInput,DateInput, PasswordInput, EmailInput

class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['Jobtitle','Company','Discription','JobDate','Salary','Region']
        widgest = {
            'Jobtitle' : TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введiть вакансiю",
            }),
            'Company': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введiть назву компанii"
            }),
            'Discription': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введiть опис вакансii"
            }),
            'JobDate': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введiть дату розмiщення вакансii"
            }),
            'Salary': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Введiть розмiр оплати"
            }),
            'Region': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введiть регiон"
            }),

        }

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
        widgets = {
            'comment': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть коментар'
            }),
        }

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логін',
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
        }

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логін',
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ім\'я',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Прізвище',
            }),
        }