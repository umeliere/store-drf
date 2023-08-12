from rest_framework import serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer to create an order
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = ('user', 'full_name', 'cc_expiry', 'cc_number',  'cc_code')
