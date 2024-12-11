from rest_framework import serializers
from ..models import CarList

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    car_name = serializers.CharField()
    car_decstr = serializers.CharField()
    active = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        # Create a new CarList instance
        return CarList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Update the CarList instance with validated data
        instance.car_name = validated_data.get('car_name', instance.car_name)
        instance.car_decstr = validated_data.get('car_decstr', instance.car_decstr)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
