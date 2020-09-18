from rest_framework import serializers
from django.contrib.auth.models import User

from supermarket_api.models.category_model import Category

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    
    def create(self, validated_data):
        user=  User.objects.create_user(username=validated_data.get("username"),
                                        password=validated_data.get("password"))
        user.save()
        return user
    
        #To Representation para manejar unit_measurement
    def to_representation(self, obj):
        new_data = {}
        new_data["id"]= obj.id
        new_data["username"]= obj.username
        return new_data