# from django.middleware.csrf import get_token
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.parsers import MultiPartParser, FormParser


class IsOwnerOrAdminPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the object or an admin
        return obj == request.user or request.user.is_staff


class ProfileModelViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    # permission_classes = (IsAuthenticated,)


def get_permissions(self):
    if self.action == "create":
        permission_classes = []
    elif self.action in ["retrieve", "update", "partial_update", "destroy"]:
        permission_classes = [IsAuthenticated, IsOwnerOrAdminPermission]
    elif self.action == "list":
        permission_classes = [IsAdminUser]
    return [permission() for permission in permission_classes]


# Generating a csrf token


# def get_csrf(request):
#     response = JsonResponse({"Info": " Success - set CSRF cookie"})
#     response["X-CSRFToken"] = get_token(request)
#     return response
