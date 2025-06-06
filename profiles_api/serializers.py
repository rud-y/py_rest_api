from rest_framework import serializers

class ExampleSerializer(serializers.Serializer):
    """Serializes a name field for testing our ExampleView"""
    name = serializers.CharField(max_length=10)
