"""Wallet URL Configuration"""

from django.urls import path
from . import views

app_name = 'wallet'

urlpatterns = [
    path('balance/', views.balanca_view, name='balance'),
    path('transactions/', views.transactions_view, name='transactions'),
]
