# Generated by Django 3.2.16 on 2022-12-20 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20221220_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='JobDate',
            field=models.DateTimeField(max_length=4, verbose_name='Дата'),
        ),
    ]
