# Generated by Django 3.2 on 2022-08-04 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Номер аккаунта')),
                ('account_type', models.IntegerField(blank=True, default=1, verbose_name='Тип аккаунта')),
            ],
            options={
                'verbose_name': 'Аккаунт',
                'verbose_name_plural': 'Аккаунты',
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите ФИО', max_length=20, verbose_name='ФИО')),
                ('citizenship', models.CharField(blank=True, default='Кыргызстан', max_length=20, verbose_name='Гражданство')),
                ('birth_year', models.DateField(verbose_name='Дата рождение')),
                ('work_place', models.CharField(blank=True, max_length=30, null=True, verbose_name='Место работы')),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.IntegerField(verbose_name='Сумма кредита')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credit.account', verbose_name='Аккаунт')),
            ],
            options={
                'verbose_name': 'Кредит',
                'verbose_name_plural': 'Кредиты',
                'db_table': 'loans',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credit.client', verbose_name='Клиент'),
        ),
    ]
