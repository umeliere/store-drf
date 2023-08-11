from django.db import models
from django.db.models import Sum, F
from django.conf import settings
from store.models import Product


class Cart(models.Model):
    """
    The model for the user cart
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        editable=False
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина пользователя {self.user}'

    def get_total_discount(self):
        """
        The method, that counts the total discount of the cart
        """
        queryset = CartItem.objects.filter(cart=self.pk).aggregate(total_cost=Sum(
            (F('product__price') * F('product__discount') / 100) * F('quantity')))['total_cost']
        return queryset

    def get_total_cost(self):
        """
        The method, that counts the total cost of the cart
        """
        queryset = CartItem.objects.filter(cart=self.pk).aggregate(
            total_cost=Sum(F('product__price') * F('quantity')))['total_cost']

        return queryset if not type(queryset) is None else queryset - self.get_total_discount()


class CartItem(models.Model):
    """
    The model for the instance of the user cart
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name='Количество')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'

    def __str__(self):
        return f'Пункт № {self.pk}'

    def total_cost(self):
        """
        The method, that counts the total cost of the user cart instance
        """
        return self.product.get_discount() * self.quantity

    def total_weight(self):
        """
        The method, that counts the total weight of the user cart instance
        """
        return self.product.weight * self.quantity
