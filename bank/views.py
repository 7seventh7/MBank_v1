from unicodedata import decimal

from django.shortcuts import render
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import *
from .serializers import *

def index(request):
    return render(request, 'bank/index.html')

class AllUsersAPIView(generics.ListAPIView):
    """All Users List"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication, )

class SingleUserAPIView(generics.RetrieveAPIView):
    """Single User Info"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication, )

class ListAccountAPI(generics.ListAPIView):
    """List of Accouns"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccauntAPIAdmin(generics.RetrieveUpdateDestroyAPIView):
    """CRUD Account by Admin"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer





class AccountAPIUser(generics.RetrieveDestroyAPIView):
    """Read and Delete Account by User"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer



class TransactionAPI(APIView):

    serializer_class = TransferSerializer
    queryset = Transfer.objects.all()
    def post (self, request):
        data = request.data
        print(data)
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)


        to_account = self.request.data['to_account']
        from_account = self.request.data['from_account']
        amount = float(self.request.data['amount'])

        try:
            balance_from = Account.objects.get(pk=from_account).balance
            balance_to = Account.objects.get(pk=to_account).balance
            f_a = Account.objects.get(pk=from_account)
            t_a = Account.objects.get(pk=to_account)
        except Exception as e:
            print(e)
            raise ValueError('No such account!!!!!')


        print('from_account=', from_account)
        print('to_account=', to_account)
        print('amount=', amount)
        print('balance_from=', balance_from)
        print('balance_to=', balance_to)

        with transaction.atomic():

            balance_from -= amount
            Account.objects.get(pk=from_account).balance = balance_from
            f_a.save()

            balance_to += amount
            Account.objects.get(pk=to_account).balance = balance_to
            t_a.save()

        print('!!!Make Transaction!!!')
        print('balance_from=', balance_from)
        print('saved balance_from=', Account.objects.get(pk=from_account).balance)
        print('balance_to=', balance_to)
        print('saved balance_to=', Account.objects.get(pk=to_account).balance)

        Transfer.objects.create(
                from_account=f_a,
                to_account=t_a,
                amount=amount,
                date=timezone.now
            )
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)












# class CreateAndCheckAccountAPI(generics.RetrieveUpdateAPIView):
#
#     queryset = Account.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)
#
#     def get_queryset(self):
#         """Return object for current authenticated user only"""
#         return self.queryset.filter(user=self.request.user)




