from django.contrib import admin

from cart.models import Cart, CartItem


class OrderItemInline(admin.TabularInline):
    model = CartItem
    raw_id_fields = ['product']
    can_delete = False
    max_num = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = (OrderItemInline,)
