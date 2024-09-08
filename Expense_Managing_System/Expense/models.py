from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.account_name} ({self.account_number})"
