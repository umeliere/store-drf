from django.contrib import admin

from cart.models import Cart, CartItem


class OrderItemInline(admin.TabularInline):
    model = CartItem
    raw_id_fields = ['product']
    can_delete = False
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = (OrderItemInline,)
