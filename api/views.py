from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from django.core.files.storage import default_storage
from django.conf import settings
from .models import *
from accounts.models import userProfile
from .serializers import *
import os
import json

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def expense(request):
    user = request.user
    items = Expense.objects.filter(user=user)
    ser = ExpenseSerializer(items, many=True, context={'user':request.user})
    return Response(ser.data)

