from catpi.cats.models import Cat
from rest_framework import serializers

class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = ["url", "name", "out"]
