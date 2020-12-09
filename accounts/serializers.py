from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ('id', 'created_at', 'user')
