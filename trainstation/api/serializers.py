from trainstation.api.models import Train, Person
from rest_framework import serializers

class TrainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Train
        fields = ['name', 'url']

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['url', 'first_name', 'last_name']
