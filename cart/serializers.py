from rest_framework import serializers

from cart.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    total_cost = serializers.FloatField()
    total_weight = serializers.FloatField()

    class Meta:
        model = CartItem
        fields = ('product', 'quantity', 'total_cost', 'total_weight')
        depth = 2


class CartSerializer(serializers.ModelSerializer):
    get_total_discount = serializers.FloatField(read_only=True)
    get_total_cost = serializers.FloatField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Cart
        fields = ('user', 'items', 'get_total_discount', 'get_total_cost')
