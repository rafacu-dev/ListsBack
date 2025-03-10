from django.urls import path

from lists.views import (ListAPIView)

urlpatterns = [
    path('', ListAPIView.as_view(),),
]