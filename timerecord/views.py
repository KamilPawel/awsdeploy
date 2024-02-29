from django.shortcuts import render
from .serializers import TimeRecord
from rest_framework import generics
from .models import Time

# Create your views here.


class TimeRecordRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Time.objects
    serializer_class = TimeRecord


class TimeRecordCreateView(generics.ListCreateAPIView):
    queryset = Time.objects
    serializer_class = TimeRecord
