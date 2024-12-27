from django.contrib.auth.models import User
from rest_framework import serializers

class UserRegistration(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(
        style={'input_type': 'password'}, write_only=True
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirmation']
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def save(self, **kwargs):
        password = self.validated_data['password']
        password_confirmation = self.validated_data['password_confirmation']
        
        # Check if passwords match
        if password != password_confirmation:
            raise serializers.ValidationError({'password_confirmation': 'Passwords do not match.'})
        
        # Check if the email already exists
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'email': 'Email already exists.'})
        
        # Create the user
        userReg = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        userReg.set_password(password)
        userReg.save()
        
        return userReg
