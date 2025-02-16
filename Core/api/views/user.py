# DJANGO IMPORTS
from django.contrib.auth import authenticate

# REST_FRAMEWORK IMPORTS
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView
)
from rest_framework.response import Response
from rest_framework import status

# LOCAL IMPORTS
from Core.api.serializers import (
    CustomUserSerializer,
    LoginSerializer
)


class CustomUserCreateAPIView(CreateAPIView):
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)
            if user:
                return Response(
                    {'message': 'Login successful', 'user': user.email},
                    status=status.HTTP_200_OK
                )
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
