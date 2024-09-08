from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BankAccountViewSet, ExpenseViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'users/<user_id>/accounts', BankAccountViewSet, basename='bankaccount')
router.register(r'users/<user_id>/accounts/<account_id>/expenses', ExpenseViewSet, basename='expense')

urlpatterns = [
    path('', include(router.urls)),
    
]