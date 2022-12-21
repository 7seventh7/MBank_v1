from django.contrib.auth.models import User
from rest_framework import serializers
from bank.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class AccountSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(slug_field='password', read_only=True)
    class Meta:
        model = Account
        fields = ('__all__')

class TransferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transfer
        fields = ('__all__')


