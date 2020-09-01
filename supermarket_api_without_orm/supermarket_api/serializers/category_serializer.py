from rest_framework import serializers
from supermarket_api.models.category_model import Category

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=140)

    def create(self, validated_data):
        category = Category()
        category.name = validated_data.get('name')
        category.description = validated_data.get('description')
        category.save()
        return category

    def update(self, category, validated_data):
        category.name = validated_data.get('name')
        category.description = validated_data.get('description')
        category.save()
        return category