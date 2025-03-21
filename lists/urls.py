from django.urls import path

from lists.views import (ListAPIView, InspiredAPIView)

urlpatterns = [
    path('', ListAPIView.as_view()),
    path('inspired/<str:listId>/', InspiredAPIView.as_view()),
]