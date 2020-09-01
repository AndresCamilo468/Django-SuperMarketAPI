from rest_framework import serializers
from supermarket_api.models.product_model import Product
from supermarket_api.models.category_model import Category
from supermarket_api.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=140)
    unit_measurement = serializers.CharField(max_length=10)
    quantity = serializers.IntegerField()
    category = serializers.IntegerField()


    #Create para validatar datos
    def create(self, validated_data):
        #Capture Dates
        product = Product()
        product.name = validated_data.get("name")
        product.description = validated_data.get("description")
        product.quantity = validated_data.get("quantity")

        #Validate unit_measurement
        try:
            um_long_to_short={"Units":"UN", "Liters":"LI", "Grams":"GR",}
            product.unit_measurement = um_long_to_short[validated_data.get("unit_measurement")]
        except Exception:
            raise ValueError('Unit Measurement Error')


        # validate category
        idCategory = validated_data.get("category")
        category = Category.objects.get(idCategory)

        if category is None:
            raise ValueError('Category Not Found')
        else:
            product.category = category
            product.save()
            return product
    

    #Update para validatar datos
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.description = validated_data.get("description")
        instance.quantity = validated_data.get("quantity")
    
        #Validate unit_measurement
        try:
            um_long_to_short={"Units":"UN", "Liters":"LI", "Grams":"GR",}
            instance.unit_measurement = um_long_to_short[validated_data.get("unit_measurement")]
        except Exception:
            raise ValueError('Unit Measurement Error')

        # validate category
        idCategory = validated_data.get("category")
        category = Category.objects.get(idCategory)

        if category is None:
            raise ValueError('Category Not Found')
        else:
            instance.category = category
            instance.save()
            return instance


    #Representation para validatar datos
    def to_representation(self, obj):
        data = {}
        
        data["id"] = obj.id
        data["name"] = obj.name
        data["description"] = obj.description
        data["quantity"] = obj.quantity
        
        um_short_to_long={"UN":"Units", "LI":"Liters", "GR":"Grams",}
        data["unit_measurement"] = um_short_to_long[obj.unit_measurement]
        
        categorySerializer = CategorySerializer(obj.category)
        data["category"] = categorySerializer.data

        
        return data