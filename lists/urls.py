from django.urls import path

from lists.views import (ListAPIView)

urlpatterns = [
    path('lists/', ListAPIView.as_view(),),
]