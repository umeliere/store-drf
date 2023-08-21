from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from cart.models import Cart, CartItem
from cart.serializers import CartSerializer, CartItemSerializer
from store.models import Product


class CartViewSet(ListModelMixin, GenericViewSet):
    """
    ViewSet for the cart
    """
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Cart.objects.get_or_create(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return self.serializer_class
        elif self.action == "add_item":
            return CartItemSerializer

    @action(methods=['post'], detail=True)
    def add_item(self, request, pk=None):
        """
        Method to add the product item
        """
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            quantity = serializer.validated_data['quantity']
            cart, cart_created = Cart.objects.get_or_create(user=self.request.user)
            product = get_object_or_404(Product, pk=self.kwargs['pk'])
            item, item_created = CartItem.objects.get_or_create(product=product, cart=cart)

            item.quantity = quantity
            item.save()

            return Response({"data": serializer.data, "status": status.HTTP_201_CREATED})

        return Response({"errors": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})

    @action(methods=['delete'], detail=True)
    def delete_item(self, request, pk=None):
        """
        Method to delete the product item
        """
        try:
            cart, _ = Cart.objects.get_or_create(user=self.request.user)
            product = get_object_or_404(Product, pk=self.kwargs['pk'])
            CartItem.objects.get(cart=cart, product=product).delete()
            return Response({"status": status.HTTP_204_NO_CONTENT})
        except ObjectDoesNotExist:
            return Response({"errors": "Данный товар не находится в корзине", "status": status.HTTP_400_BAD_REQUEST})
