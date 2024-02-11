from rest_framework import serializers
from .models import User_Form

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Form
        fields = '__all__'