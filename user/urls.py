from django.urls import path

from user.views import (GetData)

urlpatterns = [
    path('data/', GetData.as_view(), ),
]