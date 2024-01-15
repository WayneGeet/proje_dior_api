from rest_framework import serializers
from rest_framework_gis import serializers as geoSerializers
from .models import Project


class ProjectSerializer(geoSerializers.GeoFeatureModelSerializer, serializers.ModelSerializer):
    likes_count = serializers.IntegerField(read_only=True)
    user = serializers.ReadOnlyField(source='user.email')
    photo = serializers.ImageField(required=False)
    # county = serializers.ReadOnlyField()

    class Meta:
        geo_field = "location"
        model = Project
        exclude = []
