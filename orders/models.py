from django.conf import settings
from django.db import models
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.db.models import Sum, F

from store.models import Product


class Order(models.Model):
    """
    The model for the user order
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name='Пользователь'
    )
    full_name = models.CharField(max_length=100, verbose_name='Полное имя на карте')
    cc_number = CardNumberField(verbose_name='Номер карты', max_length=19)
    cc_expiry = CardExpiryField(verbose_name='Срок действия карты', max_length=5)
    cc_code = SecurityCodeField(verbose_name='Код безопасности', max_length=3)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    paid = models.BooleanField(default=False, verbose_name='Оплачено ли?')

    class Meta:
        ordering = ('created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.pk}'

    def get_total_cost(self):
        """
        The method, that counts the total cost of the order
        """
        queryset = OrderItem.objects.filter(order=self.pk).aggregate(total_cost=Sum(F('price') * F('quantity')))[
            "total_cost"]
        return f'{queryset} р.'


class OrderItem(models.Model):
    """
    The model for the instance of the user order
    """
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT, verbose_name='Заказ')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT, verbose_name='Продукт')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f'Позиция {self.pk}'
