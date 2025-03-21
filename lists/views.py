from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from django.utils.dateparse import parse_datetime

from lists.serializers import ListSerializer
from lists.models import Element, Inspired, List



class ListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        lists = List.objects.all().annotate(num_elements=Count('elements')).filter(num_elements__gt=0)
        serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            elements_data = request.data.get('elements')
            user = request.user
            date = parse_datetime(request.data.get('date'))

            if request.data.get('publishedId'):
                list_instance = List.objects.get(id=request.data.get('publishedId'), user=user)
                list_instance.elements.clear()                
                list_instance.name=request.data.get('name')
                list_instance.language=request.data.get('language')
                list_instance.visible= True if request.data.get('visibility') != "private" else False
                list_instance.hashtags=request.data.get('hashtags')
                list_instance.category=request.data.get('category')
                list_instance.date=date
            else:
            
                list_instance = List.objects.create(
                                                    user=user, 
                                                    name=request.data.get('name'), 
                                                    language=request.data.get('language'), 
                                                    visible= True if request.data.get('visibility') != "private" else False, 
                                                    hashtags=request.data.get('hashtags'), 
                                                    category=request.data.get('category'),
                                                    date=date
                                                )

            for element_data in elements_data:
                element= Element.objects.create(text=element_data.get("text"))
                list_instance.elements.add(element)

            list_instance.save()


            return Response(list_instance.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class InspiredAPIView(APIView):
    def get(self, request, listId, *args, **kwargs):
        listIds = listId.split(",")
        listReturn = []
        for id in listIds:
            listReturn.append(Inspired.objects.filter(list__id=listIds).count())

        return Response(listReturn)
    
    def post(self, request, listId, *args, **kwargs):
        list_instance = List.objects.get(id=listId)
        inspired = Inspired.objects.create(list = list_instance, user = request.user)
        return Response(True, status=status.HTTP_201_CREATED)