from rest_framework import serializers
from bank.models import Customer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')
