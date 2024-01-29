from rest_framework import serializers
from rest_framework_gis import serializers as geoSerializers
from .models import Project


class ProjectSerializer(geoSerializers.GeoFeatureModelSerializer, serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    photo = serializers.ImageField(required=False)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes_count'] = instance.likes.count()

        return representation
    # county = serializers.ReadOnlyField()

    class Meta:
        geo_field = "location"
        model = Project
        exclude = []
