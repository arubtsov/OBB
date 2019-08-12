from trainstation.api.models import Train
from rest_framework import serializers

class TrainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Train
        fields = ['name', 'url']
