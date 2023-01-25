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
    path('vacancy/<int:id>/addcomment', views.vacancy_add_comment, name='vacancy_add_comment'),
    path('comment/<int:id>/delete', views.comment_delete, name='comment_delete'),
    path('comment/<int:id>/edit', views.comment_edit, name='comment_edit'),

    path('login/', views.login, name='login_user'),
    path('logout/', views.logout, name='logout_user'),
    path('register/', views.register, name='register'),
]