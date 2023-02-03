from rest_framework import generics, status, serializers
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from customers.models import Customer
from customers.serializers import CustomerSerializer


class OrderAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        # Проверка на наличие полей в запросе
        if 'customer' in request.data and 'robot_serial' in request.data:
            email = request.data.get('customer')
            robot_serial = request.data.get('robot_serial')
        else:
            raise serializers.ValidationError()

        # Валидация Customer
        customer = CustomerSerializer(data={'email': email})
        customer.is_valid(raise_exception=True)
        customer.save()

        # Валидация Order
        serializer = self.serializer_class(data={'customer': Customer.objects.get(email=email).pk,
                                                 'robot_serial': robot_serial})
        # Проверяем данные на валидность, в случае ошибки выбрасываем исключение
        serializer.is_valid(raise_exception=True)
        # Сохраняем сериализованные данные
        serializer.save()
        # В случае успеха возвращаем ответ со статусом HTTP 201 CREATED
        return Response({'status': 'OK', 'data': serializer.data}, status=status.HTTP_201_CREATED)
