from .models import Project
from .serializers import ProjectSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'about', 'county', 'budget', 'project_type']

    # def get_queryset(self):
    #     queryset = Project.objects.all()
    #     name = self.request.query_params.get("name")
    #     if name is not None:
    #         queryset = queryset.filter(name=name)
    #     return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def get_permissions(self):
    #     if self.action in ["list", "retrieve"]:
    #         permission_classes = [permissions.IsAuthenticated]
    #     else:
    #         permission_classes = [IsOwnerOrAdminPermission]
    #     return [permission() for permission in permission_classes]


class ToggleLikeView(APIView):
    def post(self, request, pk):
        project = Project.objects.get(pk=pk)
        user = request.user

        if user in project.likes.all():
            project.likes.remove(user)
            action = "disliked"
        else:
            project.likes.add(user)
            action = "liked"
        project.likes_count = project.likes.count()  # Update likes_count
        project.save()
        serializer = ProjectSerializer(project)
        return Response({"message": f'You have {action} this project', 'project': serializer.data})
