from django.http import JsonResponse
from rest_framework import generics 
from home.models import Product
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def PostList(request):

    if request.method== 'GET':
        queryset= Product.objects.all()
        serializer_class= PostSerializer(queryset, many=True)
        return Response(serializer_class.data)
    
    if request.method =='POST':
        serializer_class= PostSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def PostDetail(request, id):

    try:
        queryset= Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method== 'GET':
        serializer_class= PostSerializer(queryset)
        return Response(serializer_class.data)
    elif request.method== 'PUT':
        serializer_class= PostSerializer(Product, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method== 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#class PostList(generics.ListCreateAPIView):
    #queryset = Product.objects.all()
    #serializer_class= PostSerializer


#class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    #queryset= Product.objects.all()
    #serializer_class= PostSerializer
