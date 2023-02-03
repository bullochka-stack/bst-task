from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Robot
from .serializers import RobotSerializer
from .services import create_excel_report


class RobotAPIView(generics.CreateAPIView):
    """
    Данный класс представляет API View для создания объекта Robot.
    """
    # Задаем набор объектов для выборки
    queryset = Robot.objects.all()
    # Указываем сериализатор, который будет использоваться для валидации данных
    serializer_class = RobotSerializer

    def post(self, request, *args, **kwargs):
        # Копируем данные из запроса
        data = request.data.copy()
        # Проверка на наличие полей model, version
        if 'model' not in data or 'version' not in data:
            return Response({'status': 'ERROR! Check all fields (model, version, created)'},
                            status=status.HTTP_400_BAD_REQUEST)
        # Добавляем новый ключ в данные
        data['serial'] = data['model'] + '-' + data['version']
        # Инициализируем сериализатор с полученными данными
        serializer = self.serializer_class(data=data)
        # Проверяем данные на валидность, в случае ошибки выбрасываем исключение
        serializer.is_valid(raise_exception=True)
        # Сохраняем сериализованные данные
        serializer.save()
        # В случае успеха возвращаем ответ со статусом HTTP 201 CREATED
        return Response({'status': 'OK', 'data': serializer.data}, status=status.HTTP_201_CREATED)


def excel_report(request):
    """
    Функция excel_report предназначена для создания и выдачи отчета в формате Excel.
    """
    file = create_excel_report()
    response = HttpResponse(file.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml"
                                                      ".sheet")
    response['Content-Disposition'] = 'attachment; filename=robots_report.xlsx'
    return response