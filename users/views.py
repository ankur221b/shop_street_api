from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.views import Response
from django.contrib.auth import authenticate, login
from users.models import Cart
from users.serializers import CartSerializer
# Create your views here.


class LoginUserApiView(APIView):

    def post(self, request):
        '''
        Login a user
        '''
        data = request.data
        print(data)
        username = None
        email = data['Email']
        password = data['Password']
        user = User.objects.get(email=email)

        if user:
            username = user.username
            auth_user = authenticate(username=username, password=password)
            if auth_user:
                login(request, auth_user)
                return Response("Success", status=status.HTTP_200_OK)
            return Response("errors", status=status.HTTP_400_BAD_REQUEST)
        return Response("errors", status=status.HTTP_400_BAD_REQUEST)


class CreateUserApiView(APIView):

    def post(self, request):
        '''
        Create a user
        '''
        data = request.data

        username, email, password = data["UserName"], data["Email"], data["Password"]
        user = User.objects.create_user(username, email, password)
        user.save()
        if user is not None:
            del data["Password"]
            return Response(data, status=status.HTTP_201_CREATED)

        return Response("Error", status=status.HTTP_400_BAD_REQUEST)


class addToCartApiView(APIView):

    def post(self, request):
        '''
        add to cart
        '''
        data = request.data
        serializer = CartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class getCartApiView(APIView):

    def post(self, request):
        '''
        add to cart
        '''
        data = request.data
        UserID = data["UserID"]
        cart = Cart.objects.filter(UserID)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ordersApiView(APIView):

    def get(self, request):
        '''
        get all orders
        '''
