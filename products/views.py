import os
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from products.helpers import convertBase64ImagetoUrl
from products.models import Product
from products.serializers import ProductSerializer
import cloudinary
# Create your views here.


class GetAllProductsApiView(APIView):

    def get(self, request):
        '''
        Get all the products
        '''
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetProductByIDApiView(APIView):

    def get(self, request, id):
        '''
        Get product by id
        '''
        product = Product.objects.filter(ProductID=id).first()
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetProductsBySearchApiView(APIView):

    def get(self, request,):
        '''
        Get product by search
        '''
        searchParam = request.GET.get("keyword")
        if not searchParam:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        product = Product.objects.filter(Title__icontains=searchParam)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddProductApiView(APIView):

    def post(self, request):
        '''
        Add product
        '''
        print(request.data)
        data = request.data
        # convertBase64ImagetoUrl(data)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
