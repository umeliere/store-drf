from django.db import transaction
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart, CartItem
from orders.models import OrderItem
from orders.serializers import OrderSerializer


class OrderCreateView(APIView):
    """
    View to create an order
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = OrderSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            with transaction.atomic():
                cart, _ = Cart.objects.get_or_create(user=self.request.user)
                items = CartItem.objects.filter(cart=cart).select_related('product')
                for item in items:
                    OrderItem.objects.create(order=serializer.save(),
                                             product=item.product,
                                             price=item.product.get_discount(),
                                             quantity=item.quantity)

                items.delete()

            return Response({"data": serializer.data, "status": status.HTTP_201_CREATED})

        return Response({"errors": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})
