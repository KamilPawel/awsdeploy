from rest_framework import serializers
from .models import Time

class TimeRecord(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Time
