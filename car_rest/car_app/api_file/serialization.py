from rest_framework import serializers

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    car_name = serializers.CharField()
    car_decstr = serializers.CharField()
    active = serializers.BooleanField(read_only=True)