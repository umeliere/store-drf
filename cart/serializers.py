from rest_framework import serializers

from cart.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the cart item
    """
    product = serializers.PrimaryKeyRelatedField(read_only=True)
    quantity = serializers.IntegerField(default=1)

    class Meta:
        model = CartItem
        fields = ('product', 'quantity', 'total_cost', 'total_weight')


class CartSerializer(serializers.ModelSerializer):
    """
    Serializer for the cart
    """
    items = CartItemSerializer(many=True, read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Cart
        fields = ('user', 'items', 'get_total_discount', 'get_total_cost')
