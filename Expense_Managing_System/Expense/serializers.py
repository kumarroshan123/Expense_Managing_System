from django.contrib.auth.models import User
from rest_framework import serializers
from .models import BankAccount

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['user', 'account_number', 'account_name', 'balance']

    