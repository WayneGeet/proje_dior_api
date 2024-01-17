from rest_framework import serializers
from .models import Profile
from rest_framework.validators import ValidationError


class ProfileSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = "__all__"
