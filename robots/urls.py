from django.urls import path
from .views import RobotAPIView

urlpatterns = [
    path('add-robot/', RobotAPIView.as_view()),
]
