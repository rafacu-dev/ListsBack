from lists.models import Element, List
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField


class ElementSerializer(ModelSerializer):
    class Meta:
        model = Element
        fields = ['id', 'text', 'checked']

class ListSerializer(ModelSerializer):
    elements = ElementSerializer(many=True)
    user = PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = List
        fields = ['id', 'name', 'category', 'elements', 'date', 'user']
    