from django.conf import settings
from django.contrib.auth import get_user_model
from rest_auth.models import TokenModel
from rest_framework import serializers
from user.models import Courier, Profiles


class ProfileRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    balance = serializers.IntegerField()
    dob = serializers.DateField()

    def create(self, validated_data):
        user = get_user_model().objects.create(username=validated_data.get('username'))
        user.set_password(validated_data.get('password'))
        user.save()
        TokenModel.objects.create(user=user)
        profile = Profiles.objects.create(
            user=user,
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            balance=validated_data.get('balance'),
            dob=validated_data.get('dob'),
        )
        return profile


class ProfileLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class CourierRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    car = serializers.CharField()


    def create(self, validated_data):
        user = get_user_model().objects.create(username=validated_data.get('username'))
        user.set_password(validated_data.get('password'))
        user.save()
        TokenModel.objects.create(user=user)
        courier = Courier.objects.create(
            user=user,
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            car=validated_data.get('car'),
        )
        return courier


