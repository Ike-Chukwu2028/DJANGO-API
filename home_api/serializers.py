from rest_framework import serializers
from home.models import Product

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Product
        fields = '__all__'
        #fields= ['name', 'image', 'description', 'price']
