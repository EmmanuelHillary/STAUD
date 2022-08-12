from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from .serializers import OrderSerializer, OrderInlineSerializer
from .models import Order
from rest_framework.permissions import AllowAny


class OrderListCreateAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        qs = Order.objects.all()
        serializer = OrderInlineSerializer(qs)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        print(data)
        serialized_data = OrderSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
        return Response({"success": "Your order was successful"})
