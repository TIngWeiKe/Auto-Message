from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *
from .models import *
from utils.decorators import *
from utils.exceptions import *


class AccountViewSet(
        mixins.CreateModelMixin,
        viewsets.GenericViewSet):
    permission_classess = (IsAuthenticated, )
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @DRF_response
    def list(self, request):
        queryset = self.queryset.filter(is_removed=False)
        serializer = self.get_serializer(queryset, many=True, partial=True)
        payload = serializer.data

        return payload

    @DRF_response
    def create(self, request):
        from django.contrib.auth.models import Permission

        name = request.data.get('name', None)
        password = request.data.get('password', None)
        email = request.data.get('email', None)

        if Account.objects.filter(email=email).exists():
            raise AlreadyExistError(f"Account Already Existed ({email})")

        if name is None or password is None or email is None:
            raise MissingInputError

        user = User.objects.create_user(
            username=email,
            password=password
        )

        acc, created = Account.objects.get_or_create(
            email=email, name=name, user=user)

        serializer = self.get_serializer(acc)
        payload = serializer.data

        return payload, 201

    @DRF_response
    def update(self, request, *args, **kwargs):
        import json

        instance = self.get_object()
        name = request.data.get('name', None)

        if name is None:
            raise MissingInputError

        instance.name = name
        instance.save(update_fields=["name"])
        serializer = self.get_serializer(instance)

        return serializer.data, 201


@api_view(["POST"])
@json_response
def login(request):
    import json
    from django.contrib import auth

    data = request.data
    username = data.get('username', None)
    password = data.get('password')

    if username is None or password is None:
        raise MissingInputError('username, password')

    user = auth.authenticate(username=username, password=password)

    if user is None:
        raise UserError("Invalid credentials.")

    auth.login(request, user)
