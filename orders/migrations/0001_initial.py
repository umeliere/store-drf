# Generated by Django 4.2.1 on 2023-08-15 13:42

import creditcards.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Полное имя на карте')),
                ('cc_number', creditcards.models.CardNumberField(max_length=19, verbose_name='Номер карты')),
                ('cc_expiry', creditcards.models.CardExpiryField(max_length=5, verbose_name='Срок действия карты')),
                ('cc_code', creditcards.models.SecurityCodeField(max_length=3, verbose_name='Код безопасности')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачено ли?')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='orders.order', verbose_name='Заказ')),
            ],
        ),
    ]
