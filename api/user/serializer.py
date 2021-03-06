from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    locality_name = serializers.CharField(
        source="locality.name", read_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)

        instance.save()
        return instance

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = (
            'id', 'name', 'email', 'password', 'phone', 'house_number',
            'locality', 'locality_name', 'payment', 'recurring_product'
        )
        read_only_field = ('is_active', 'created', 'modified')


class UserListSerializer(serializers.ModelSerializer):
    locality_name = serializers.CharField(
        source="locality.name", read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'locality', 'house_number', 'locality_name')


class UserRetrieveSerializer(serializers.ModelSerializer):
    locality_name = serializers.CharField(
        source="locality.name", read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'name', 'email', 'phone', 'house_number', 'locality',
            'locality_name', 'payment', 'recurring_product'
        )
