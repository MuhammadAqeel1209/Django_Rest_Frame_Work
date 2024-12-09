from rest_framework import routers, serializers, viewsets

class carSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    car_name = serializers.CharField()
    car_decstr = serializers.CharField()
    active = serializers.BooleanField(read_only=True)
    