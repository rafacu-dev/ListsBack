from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.utils.dateparse import parse_datetime

from lists.serializers import ListSerializer
from lists.models import Element, List



class ListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        lists = List.objects.all()
        serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = ListSerializer(data=request.data)

        print("***********************", request.data)
        if serializer.is_valid():
            elements_data = request.data.get('elements')
            user = request.user
            date = parse_datetime(request.data.get('date'))    
            list_instance = List.objects.create(
                                                user=user, 
                                                name=request.data.get('name'), 
                                                category=request.data.get('category'),
                                                date=date
                                            )
            for element_data in elements_data:
                element= Element.objects.create(text=element_data.get("text"))
                list_instance.elements.add(element)
            list_instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)