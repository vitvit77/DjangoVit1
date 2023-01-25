from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Vacancy, Comments
from .forms import VacancyForm, CommentForm, RegisterForm, LoginForm
from django.contrib.auth.hashers import make_password
from django.contrib import auth


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
    if not request.user.is_authenticated:
        return redirect('login_user')
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            return redirect('home')
    form = VacancyForm()
    context = {
        'form': form
    }
    return render(request, "main/create.html", context)

def vacancy_view(request, id=1):
    print('id',id)
    OneJob = Vacancy.objects.get(id=id)
    print(':::',Comments)
    return render(request, 'main/vacancy_view.html', {
        'title': 'Перегляд оголошення',
        'OneJob': OneJob,
        'comments': Comments.objects.filter(vacancy_id=id),
        'comment_form': CommentForm
    })


def vacancy_edit(request, id=0):
    if not request.user.is_authenticated:
        return redirect('login_user')
    if request.method == 'GET':
        if id == 0:
            form = VacancyForm()
        else:
            OneJob = Vacancy.objects.get(id=id)
            if request.user.id != OneJob.user.id:
                return redirect('main')
            form = VacancyForm(instance=OneJob)
        return render(request, "main/vacancy_edit.html", {'form':form})
    else:
        if id == 0:
            form = VacancyForm(request.POST)
        else:
            OneJob = Vacancy.objects.get(id=id)
            if request.user.id != OneJob.user.id:
                return redirect('main')
            form = VacancyForm(request.POST, instance=OneJob)
        if form.is_valid():
            form.save()
        return redirect('main')

def vacancy_del(request, id =0 ):
    if not request.user.is_authenticated:
        return redirect('login_user')
    OneJobDel = Vacancy.objects.get(id=id)
    if request.user.id != OneJobDel.user.id:
        return redirect('main')
    OneJobDel.delete()
    AllJobs = Vacancy.objects.all()
    return render(request, "main/index_tab.html", {'title': 'Перелiк вакансiй', 'AllJobs': AllJobs})

def vacancy_add_comment(request, id=0):
    if not request.user.is_authenticated:
        return redirect('login_user')
    if request.POST:
        form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.vacancy = Vacancy.objects.get(id=id)
        comment.user = request.user
        form.save()
    return redirect('/vacancy/%s/view/' % id)

def comment_delete(request, id=0):
    if not request.user.is_authenticated:
        return redirect('login_user')
    comment = Comments.objects.get(id=id)
    if request.user.id == comment.user.id:
        comment.delete()
    return redirect('/vacancy/%s/view/' % comment.vacancy_id)

def comment_edit(request, id=0):
    if not request.user.is_authenticated:
        return redirect('login_user')
    if request.method == 'GET':
        if id == 0:
            form = CommentForm()
        else:
            comment = Comments.objects.get(id=id)
            if request.user.id != comment.user.id:
                return redirect('all_posts')
            form = CommentForm(instance=comment)
        return render(request, 'main/comment_edit.html', {'form': form})
    else:
        if id == 0:
            form = CommentForm(request.POST)
        else:
            comment = Comments.objects.get(id=id)
            if request.user.id != comment.user.id:
                return redirect('all_posts')
            form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
        return redirect('/vacancy/%s/view/' % comment.vacancy_id)

def logout(request):
    auth.logout(request)
    request.session.flush()
    return redirect('home')

def login(request):
    args = {}
    form = LoginForm(request.POST)
    args['form'] = form
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            args['login_error'] = 'user not found'
            return render(request, 'registration/login.html', args)
    return render(request, 'registration/login.html',args)

def register(request):
    args = {}
    form = RegisterForm()
    args['form'] = form
    if request.POST:
        newUserForm = RegisterForm(request.POST)
        if newUserForm.is_valid():
            form = newUserForm.save(commit=False)
            form.password = make_password(form.password)
            form.save()
            new_user = auth.authenticate(username=newUserForm.cleaned_data['username'],
                                         password=newUserForm.cleaned_data['password'])
            auth.login(request, new_user)
            return redirect('home')
        else:
            args['form'] = newUserForm
    return render(request, 'registration/register.html',args)