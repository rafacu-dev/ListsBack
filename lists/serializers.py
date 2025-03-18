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
    
    def create(self, validated_data):
        elements_data = validated_data.pop('elements')
        print("*********************",self.context)
        user = self.context['request'].user
        list_instance = List.objects.create(user=user, **validated_data)
        for element_data in elements_data:
            element, _ = Element.objects.get_or_create(**element_data)
            list_instance.elements.add(element)
        return list_instance