from django.urls import path
from .views import RobotAPIView, excel_report

urlpatterns = [
    path('add-robot/', RobotAPIView.as_view()),
    path('excel-report/', excel_report)
]
