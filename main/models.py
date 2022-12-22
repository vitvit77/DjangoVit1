from django.db import models

class Vacancy(models.Model):
    Jobtitle = models.CharField('Посада',max_length=100)
    Company = models.CharField('Компания',max_length=50)
    Discription = models.TextField('Опис', )
    JobDate = models.CharField ('Дата', max_length=10)
    Salary = models.IntegerField('Заробiтна плата')
    Region = models.CharField('Регiон',max_length=30)

    def __str__(self):
        return str(self.Salary)
    class Meta:
        verbose_name = 'Записи о вакансиях'
        verbose_name_plural = 'Записи о вакансиях'