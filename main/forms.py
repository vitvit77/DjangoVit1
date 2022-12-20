from .models import Vacancy
from django.forms import ModelForm, TextInput, Textarea, NumberInput,DateInput

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
