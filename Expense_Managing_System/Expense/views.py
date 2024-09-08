from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User 
from .models import BankAccount
from .serializers import UserSerializer , BankAccountSerializer , ExpenseSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BankAccountViewSet(viewsets.ModelViewSet):
    serializer_class = BankAccountSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return BankAccount.objects.filter(user_id=user_id)

    

    

    
