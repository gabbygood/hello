from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'name',
            'password',
            'profilePicture',
            'phone_number',     # ✅ Added
            'birth_date'        # ✅ Added
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'profilePicture': {'required': False},
            'phone_number': {'required': False, 'allow_null': True, 'allow_blank': True},
            'birth_date': {'required': False, 'allow_null': True},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
