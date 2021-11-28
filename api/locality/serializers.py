from rest_framework import serializers

from .models import Locality


class LocalitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Locality
        fields = ['id', 'name']
