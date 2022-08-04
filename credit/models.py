from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО', help_text='Введите ФИО')
    citizenship = models.CharField(max_length=20, verbose_name='Гражданство', default='Кыргызстан', blank=True)
    birth_year = models.DateField(verbose_name='Дата рождение')
    work_place = models.CharField(max_length=30, verbose_name='Место работы',  blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        db_table = 'customers'

    def __str__(self):
        return self.name

class Account(models.Model):
    number = models.CharField(max_length=16, unique=True, verbose_name='Номер аккаунта')
    account_type = models.IntegerField(default=1, verbose_name='Тип аккаунта')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')


    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
        db_table = 'accounts'

    def __str__(self):
        return self.number

class Credit(models.Model):
    sum = models.IntegerField(verbose_name='Сумма кредита')
    date = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Аккаунт')


    class Meta:
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'
        db_table = 'loans'

    def __str__(self):
        return f'{self.sum}'

