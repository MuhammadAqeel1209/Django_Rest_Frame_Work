from rest_framework import serializers
from ..models import CarList, ShowRoom,Reivew


class ReiviewSerializer(serializers.ModelSerializer):
    apiUser = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Reivew
        exclude =('car',)
        # fields = "__all__"  # Include all fields from the Reivew model
class CarSerializer(serializers.ModelSerializer):
    # Custom Serializer 
    discount_price = serializers.SerializerMethodField()

    reiviews = ReiviewSerializer(many=True,read_only=True)
    class Meta:
        model = CarList
        fields = "__all__"  # Include all fields from the CarList model

    def get_discount_price(self, obj):
        if obj.price is None:
            return None  # Handle None price gracefully
        discount = obj.price - 5000  # Fixed discount of 5000
        return discount

    # Validate price for specific conditions
    def validate_price(self, value):
        if value <= 20000.00:
            raise serializers.ValidationError("Price must be more than 20,000.")
        return value

    # Object-level validation
    def validate(self, data):
        if data["car_name"] == data["car_decstr"]:
            raise serializers.ValidationError(
                "Car name and description cannot be the same."
            )
        return data

class ShowroomSerializer(serializers.ModelSerializer):
    # showrooms = CarSerializer(many=True,read_only=True)
    # showrooms = serializers.StringRelatedField(many=True)
    # showrooms =serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    showrooms = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='car_detail'
    )
    class Meta:
        model = ShowRoom
        fields = "__all__" 



# That Code by Hand 

# id = serializers.IntegerField(read_only=True)
    # car_name = serializers.CharField()
    # car_decstr = serializers.CharField()
    # active = serializers.BooleanField(read_only=True)
    # car_number = serializers.CharField(validators=[alphanumeric])
    # price = serializers.DecimalField(max_digits=9, decimal_places=2)

    # def create(self, validated_data):
    #     # Create a new CarList instance
    #     return CarList.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     # Update the CarList instance with validated data
    #     instance.car_name = validated_data.get("car_name", instance.car_name)
    #     instance.car_decstr = validated_data.get("car_decstr", instance.car_decstr)
    #     instance.active = validated_data.get("active", instance.active)
    #     instance.car_number = validated_data.get("car_number", instance.car_number)
    #     instance.price = validated_data.get("price", instance.price)
    #     instance.save()

