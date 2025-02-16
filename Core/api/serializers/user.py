# REST_FRAMEWORK IMPORTS
from rest_framework import serializers

# LOCAL IMPORTS
from Core.models import CustomUser, UserCategory


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    category = serializers.ChoiceField(
        choices=UserCategory.Category.choices,
        default=UserCategory.Category.STUDENT
    )

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'full_name',
            'password',
            'category'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        category_data = validated_data.pop(
            'category', UserCategory.Category.STUDENT
        )
        user = CustomUser.objects.create_user(
            id=validated_data['id'],
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=validated_data['password']
        )
        UserCategory.objects.create(user=user, category=category_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True, min_length=8, style={'input_type': 'password'}
    )

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError(
                "Email and password are required"
            )

        user = CustomUser.objects.filter(email=email).first()
        if user and user.check_password(password):
            return data
        else:
            raise serializers.ValidationError("Invalid credentials")
