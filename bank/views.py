from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from .models import *
from .serializers import UserSerializer


def index(request):
    return render(request, 'bank/index.html')

class UserAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = UserSerializer

class A(APIView):
    pass
