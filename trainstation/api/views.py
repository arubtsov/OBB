from django.shortcuts import render
from rest_framework import viewsets

from trainstation.api.models import Train, Person
from trainstation.api.serializers import TrainSerializer, PersonSerializer


class TrainViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trains to be viewed or edited.
    """
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed or edited.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
