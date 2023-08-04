from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet

from cart.models import Cart
from cart.serializers import CartSerializer


class CartViewSet(ListModelMixin, GenericViewSet):
    serializer_class = CartSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return Cart.objects.get_or_create(user=self.request.user)
