from rest_framework import serializers
from ..models import CarList

# Validators
def alphanumeric(value):
    if not value.isalnum():
        raise serializers.ValidationError("Car number should be alphanumeric.")
    return value


# Model Serilizer make the table automatic by using that method 
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarList
        fields = "__all__" # Want when all columns are available
        # fields = ["id",'car_name','car_decstr']   # Want When Specific Column
        # exclude =['car_name']
        
        
          
    # Validate for Specific Columns
    def validate_price(self, value):
        if value <= 20000.00:
            raise serializers.ValidationError("Price must be more than 20,000.")
        return value

    # Object Validation
    def validate(self, data):
        if data["car_name"] == data["car_decstr"]:
            raise serializers.ValidationError(
                "Car name and description cannot be the same."
            )
        return data
    
    



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

