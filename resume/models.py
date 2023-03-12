from django.contrib.auth.models import User
from django.db import models


class Resume(models.Model):
    """
    Модель резюме пользователя
    """

    class Status(models.IntegerChoices):
        active = 1, 'Активно ищу работу'
        reviewing_offers = 2, 'Рассматриваю предложения'
        archived = 3, 'Архив'

    status = models.PositiveSmallIntegerField(verbose_name='Статус', choices=Status.choices, default=Status.active)
    grade = models.CharField(verbose_name='Уровень резюме', max_length=50)
    specialty = models.CharField(verbose_name='Специальность', max_length=50)
    salary = models.PositiveIntegerField(verbose_name='Зарплата', null=True, blank=True)
    education = models.CharField(verbose_name='Образование', max_length=50)
    experience = models.TextField(verbose_name='Опыт')
    portfolio = models.URLField(verbose_name='Портфолио', null=True, blank=True)
    title = models.CharField(verbose_name='Название', max_length=35)
    phone = models.CharField(verbose_name='Номер телефона', max_length=11)
    email = models.EmailField(verbose_name='Email')
    author = models.ForeignKey(User, verbose_name='Автор', related_name='resume', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
