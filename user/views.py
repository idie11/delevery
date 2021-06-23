from rest_auth.models import TokenModel
from rest_framework import status
from rest_framework.generics import CreateAPIView,GenericAPIView
from rest_framework.response import Response
from .permissions import IsUserOwnerOrReadOnly

from user.serializers import CourierRegisterSerializer, ProfileRegisterSerializer, ProfileLoginSerializer
from django.contrib.auth import (
    login as django_login,
    logout as django_logout, authenticate
)


class ProfileRegisterView(CreateAPIView):
    serializer_class = ProfileRegisterSerializer
    permission_classes = (IsUserOwnerOrReadOnly, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response('success', status=status.HTTP_201_CREATED)


class ProfileLoginView(GenericAPIView):
    serializer_class = ProfileLoginSerializer
    permission_classes = (IsUserOwnerOrReadOnly, )


    def post(self, request, *args, **kwargs):
        serializer = ProfileLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            token = TokenModel.objects.get(user=user)
            return Response({'key': token.key}, status=status.HTTP_201_CREATED)
        return Response('invalid login', status=status.HTTP_401_UNAUTHORIZED)


class CourierRegisterView(CreateAPIView):
    serializer_class = CourierRegisterSerializer
    permission_classes = (IsUserOwnerOrReadOnly, )


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response('success', status=status.HTTP_201_CREATED)

    