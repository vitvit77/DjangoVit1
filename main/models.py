from django.db import models
from django.contrib.auth.models import User
class Vacancy(models.Model):
    Jobtitle = models.CharField('Посада',max_length=100)
    Company = models.CharField('Компания',max_length=50)
    Discription = models.TextField('Опис', )
    JobDate = models.CharField ('Дата', max_length=10)
    Salary = models.IntegerField('Заробiтна плата')
    Region = models.CharField('Регiон',max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.Salary)
    class Meta:
        verbose_name = 'Записи о вакансиях'
        verbose_name_plural = 'Записи о вакансиях'

class Comments(models.Model):
    class Meta:
        db_table = 'comments'
    id = models.AutoField('CommentId', primary_key=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Коментар')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField('CreateDate', auto_now=True)