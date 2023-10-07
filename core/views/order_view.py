from rest_framework.viewsets import ModelViewSet

from core.models import Order
from core.serializers import OrderCreateSerializer, OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return OrderSerializer
        return OrderCreateSerializer

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="admin"):
            return Order.objects.all()
        return Order.objects.filter(client=user)
