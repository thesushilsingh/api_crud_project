from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.serializers import ItemSerializer
from django.shortcuts import get_object_or_404
from app.models import Product


class ApiHomePage(APIView):
    def get(self, request, id=None):
        if id:
            product = Product.objects.get(id=id)
            return Response(ItemSerializer(product).data, status=status.HTTP_200_OK)
        else:
            products = Product.objects.all()
            serialized_data = [ItemSerializer(product).data for product in products]
            return Response(serialized_data, status=status.HTTP_200_OK)
        

    def post(self, request, id=None):
        if id:
            product = Product.objects.get()
        else:
            product_data = request.data
            product = ItemSerializer(data=product_data)
            if product.is_valid():
                product.save()
                return Response(product.data, status=status.HTTP_201_CREATED)
            else:
                return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def put(self, request, id=None):
        if id:
            product = Product.objects.get(id=id)    
            product_data = request.data
            product_serializer = ItemSerializer(product, data=product_data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        product = get_object_or_404(Product, id=id)
        product_data = request.data
        product_serializer = ItemSerializer(product, data=product_data, partial=True)

        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

    def delete(self, request, id=None):
        if id:
            product = Product.objects.get(id=id)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)