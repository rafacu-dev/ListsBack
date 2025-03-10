from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from lists.serializers import ListSerializer
from lists.models import List



class ListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        lists = List.objects.all()
        serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)