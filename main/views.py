from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Vacancy
from .forms import VacancyForm


def index(request):
    AllJobs = Vacancy.objects.all()
    return render(request, "main/index.html", {'title': 'Головна строрiнка', 'AllJobs' : AllJobs})

def index_tab(request):
    AllJobs = Vacancy.objects.all()
    return render(request, "main/index_tab.html", {'title': 'Перелiк вакансiй', 'AllJobs' : AllJobs})
def about(request):
    return render(request, "main/about.html")

def create(request):
    error = ''

    if request.method == 'POST':
        form = VacancyForm(request.POST)
        print(form)
        if form.is_valid():

            form.save()
            return redirect('home')
    form = VacancyForm()
    context = {
        'form': form
    }
    return render(request, "main/create.html", context)

def vacancy_view(request, id=1):
    OneJob = Vacancy.objects.get(id=id)
    #print(OneJob.id)
    return render(request, "main/vacancy_view.html", {'title': 'Перегляд оголошення', 'OneJob': OneJob})


def vacancy_edit(request, id=0):

    if request.method == 'GET':
        if id == 0:
            form = VacancyForm()
        else:
            OneJob = Vacancy.objects.get(id=id)
            form = VacancyForm(instance=OneJob)
        return render(request, "main/vacancy_edit.html", {'form':form})
    else:
        if id == 0:
            form = VacancyForm(request.POST)
        else:
            OneJob = Vacancy.objects.get(id=id)
            form = VacancyForm(request.POST, instance=OneJob)
        if form.is_valid():
            form.save()
        return redirect('main')

def vacancy_del(request, id =0 ):
    OneJobDel = Vacancy.objects.get(id=id)
    OneJobDel.delete()
    AllJobs = Vacancy.objects.all()
    return render(request, "main/index_tab.html", {'title': 'Перелiк вакансiй', 'AllJobs': AllJobs})
