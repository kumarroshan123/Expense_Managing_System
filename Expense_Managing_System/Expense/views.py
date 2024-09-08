from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User 
from .models import BankAccount, Expenses
from .serializers import UserSerializer , BankAccountSerializer , ExpenseSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BankAccountViewSet(viewsets.ModelViewSet):
    serializer_class = BankAccountSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return BankAccount.objects.filter(user_id=user_id)
    
    def perform_create(self, serializer):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        serializer.save(user=user)

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        account_id = self.kwargs['account_id']
        return Expenses.objects.filter(account__user_id=user_id, account_id=account_id)

    

    
