from projects.models import Project
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.validators import ValidationError


User = get_user_model()


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=40)

    def check_user(self, clean_data):
        user = authenticate(
            email=clean_data["email"], password=clean_data["password"])
        if user is None:
            raise ValidationError("User not found")
        return user


class UserSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)
    liked_projects = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name',
                  'last_name', 'id_no', 'password', 'projects', 'liked_projects')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get(
            "first_name", instance.first_name)
        instance.last_name = validated_data.get(
            "last_name", instance.last_name)
        instance.id_no = validated_data.get(
            "id_no", instance.id_no)
        instance.save()

        return instance
