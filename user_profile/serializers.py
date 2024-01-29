from rest_framework import serializers
from .models import Profile
from rest_framework.validators import ValidationError


class ProfileSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField(source="user.email")
    first_name = serializers.ReadOnlyField(source="user.first_name")
    last_name = serializers.ReadOnlyField(source="user.last_name")
    id_no = serializers.ReadOnlyField(source="user.id_no")
    photo = serializers.ImageField(required=False)

    class Meta:
        model = Profile
        fields = "__all__"
