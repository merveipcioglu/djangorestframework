# serializers.py
from rest_framework import serializers
from .models import UserRentIhaHistory

class UserRentIhaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRentIhaHistory
        fields = ['user', 'iha', 'startDate', 'finishDate','startTime','finishTime' ]

class UserRentIhaHistoryDeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()         

class UserRentIhaHistoryListSerializer(serializers.Serializer):
    id = serializers.IntegerField()       


class UserRentIhaHistoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRentIhaHistory
        fields = ['startDate', 'finishDate', 'startTime', 'finishTime']
