from accounts.models import *
from rest_framework import serializers

class userProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = userProfile
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    user = userProfileSerializer(many=False)
    
    class Meta:
        model = Expense
        fields = '__all__'