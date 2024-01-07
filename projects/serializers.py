from rest_framework import serializers
from rest_framework_gis import serializers as geoSerializers
from .models import Project, Likes


class LikesSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    project_name = serializers.SerializerMethodField()

    class Meta:
        model = Likes
        exclude = []

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['casted_votes'] = instance.confidence_level.count()
    #     return representation

    def get_user_name(self, instance):
        return instance.user.first_name

    def get_project_name(self, instance):
        return instance.project.name


class ProjectSerializer(geoSerializers.GeoFeatureModelSerializer, serializers.ModelSerializer):
    project_likes = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Likes.objects.all())
    user = serializers.ReadOnlyField(source='user.email')
    photo = serializers.ImageField(required=False)

    class Meta:
        geo_field = "location"
        model = Project
        exclude = []
