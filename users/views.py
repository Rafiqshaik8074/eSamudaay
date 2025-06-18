from django.shortcuts import render

# Create your views here.

# users/views.py

from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Customer
from .serializers import LoginSerializer, CustomerSerializer

class LoginAPI(APIView):
    def post(self, request):
        print('Data from client: ', request.body)
        print('Data from Client2: ', request.data)
        serializer = LoginSerializer(data=request.data)
        # print('Login Data: ', serializer)
        if serializer.is_valid():
            print('------------ It iw working ----------------')
            print('Email ::: ', serializer.validated_data['email'])
            print('Password ::: ', serializer.validated_data['password'])
            user = authenticate(
                email=serializer.validated_data['email'],
                
                password=serializer.validated_data['password']
            )
            print('User ::: ', user)
            if user:
                # token, created = Token.objects.get_or_create(user=user)
                # return Response({'token': token.key})
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.contrib.auth.hashers import check_password
from .models import Customer

class LoginAPI2(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                customer = Customer.objects.get(email=email)
                if customer.password == password:  # Basic match (not secure)
                    return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)
            except Customer.DoesNotExist:
                return Response({'error': 'Email not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class AddCustomerAPI(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerListAPI(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)