from lists.models import Element, Inspired, List
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, SerializerMethodField


class ElementSerializer(ModelSerializer):
    class Meta:
        model = Element
        fields = ['id', 'text', 'checked']


class ListSerializer(ModelSerializer):
    elements = ElementSerializer(many=True)
    user = PrimaryKeyRelatedField(read_only=True)
    
    inspired=SerializerMethodField('get_inspired')

    class Meta:
        model = List
        fields = ['id', 'name', 'category', 'elements', 'date', 'user', "inspired"]
    
    def get_inspired(self,l:List):
        return Inspired.objects.filter(list = l).count()