from rest_framework import serializers
from .models import User_Form
from django.core.validators import RegexValidator

# Serializers define the API representation.
class UserFormSerializer(serializers.ModelSerializer):

    phone_number = serializers.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])

    class Meta:
        model = User_Form
        fields = ('id','name','date_of_birth','email','phone_number')

    def create(self, validated_data):
        return User_Form.objects.create(**validated_data)