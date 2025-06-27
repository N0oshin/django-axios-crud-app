# A serializer in Django Rest Framework (DRF) is a component that handles serialization and deserialization. It converts your database model into JSON format (serialization) or takes JSON data as input, validates it, and translates it into a Django model instance (deserialization).

from rest_framework import serializers
from .models import item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = "__all__"
