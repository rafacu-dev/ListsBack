from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from user.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class GetData(APIView):
    def get(self, request, format=None):
        user = self.request.user

        try:
            data_return = UserCreateSerializer(user).data
            return Response(data_return,status=status.HTTP_200_OK)
            
        except Exception as e: 
            print(e) 
            return Response(
                {"error": 'Error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
