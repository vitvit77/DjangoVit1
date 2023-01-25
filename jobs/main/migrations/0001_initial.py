# Generated by Django 3.2.16 on 2022-12-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jobtitle', models.CharField(max_length=30, verbose_name='Посада')),
                ('Discription', models.TextField(verbose_name='Опис')),
                ('JobDate', models.DateTimeField()),
                ('Salary', models.IntegerField(verbose_name='Зарплата')),
                ('Region', models.CharField(max_length=30, verbose_name='Регион')),
            ],
        ),
    ]