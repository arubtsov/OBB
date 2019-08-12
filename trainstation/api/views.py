from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from trainstation.api.models import Train, Person
from trainstation.api.serializers import TrainSerializer, PersonSerializer


class TrainViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trains to be viewed or edited.
    """
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    
    @action(detail=True, methods=['get'])
    def passengers(self, request, pk=None):
        """Get all passengers on board."""
        train = self.get_object()

        queryset = train.get_passengers()
        serializer = PersonSerializer(queryset, many=True, context={'request': request})

        return Response(serializer.data)


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed or edited.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
