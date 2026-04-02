from catpi.cats.models import Cat
from rest_framework import viewsets

from catpi.cats.serializers import CatSerializer

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all().order_by("name")
    serializer_class = CatSerializer
