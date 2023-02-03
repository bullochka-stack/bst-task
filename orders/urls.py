from django.urls import path
from .views import OrderAPIView

urlpatterns = [
    path('add-order/', OrderAPIView.as_view()),
]
