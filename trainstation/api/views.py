from django.shortcuts import render
from rest_framework import viewsets

from trainstation.api.models import Train
from trainstation.api.serializers import TrainSerializer


class TrainViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    
