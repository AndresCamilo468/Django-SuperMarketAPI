from rest_framework import serializers
from supermarket_api.models.category_model import Category 


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'owner']

    
    def to_representation(self, obj):
        data = super().to_representation(obj)
        
        data["owner"] = {
            "id"        :obj.owner.id,
            "username" : obj.owner.username
        }
        
        return data