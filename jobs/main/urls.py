from django.urls import path
from .import views


urlpatterns = [
    path('', views.index_tab, name='main'),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('vacancy/<int:id>/view/', views.vacancy_view, name='vacancy_view'),
    path('vacancy/<int:id>/edit/', views.vacancy_edit, name='vacancy_edit'),
    path('vacancy/<int:id>/del/', views.vacancy_del, name='vacancy_del'),
]