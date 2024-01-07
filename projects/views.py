from .models import Project, Likes
from .serializers import ProjectSerializer, LikesSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import JSONParser


class IsOwnerOrAdminPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is the owner of the object or an admin
        return obj.user == request.user or request.user.is_staff


class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsOwnerOrAdminPermission]
        return [permission() for permission in permission_classes]


class LikesModelViewSet(ModelViewSet):
    serializer_class = LikesSerializer
    queryset = Likes.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, pk):
        likes_instance = Likes.objects.get(pk=pk)
        serializer = LikesSerializer(
            likes_instance, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
