# from django.middleware.csrf import get_token
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import Http404
from rest_framework import viewsets


class IsOwnerOrAdminPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the object or an admin
        return obj == request.user or request.user.is_staff


class ProfileModelViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (IsOwnerOrAdminPermission,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = "slug"
    http_method_names = ["put", "get",]

    # def get_profile_by_slug(self, slug):
    #     try:
    #         return Profile.objects.get(slug=slug)
    #     except Profile.DoesNotExist:
    #         raise Http404("Profile not found")

    # def get(self, request, slug=None):
    #     profile = self.get_profile_by_slug(slug)
    #     serializer = ProfileSerializer(profile)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    # def put(self, request, slug=None):
    #     profile = self.get_profile_by_slug(slug)
    #     data = request.data
    #     serializer = ProfileSerializer(profile, data=data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data={"profile updated successfully"}, status=status.HTTP_204_NO_CONTENT)
    #     return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, slug=None):
    #     profile = self.get_profile_by_slug(slug)
    #     profile.delete()
    #     return Response(data={"message": "profile deleted successfully"}, status=status.HTTP_200_OK)

    # def get_permissions(self):
    #     if self.action == "create":
    #         permission_classes = []
    #     elif self.action in ["retrieve", "update", "partial_update", "destroy"]:
    #         permission_classes = [IsAuthenticated, IsOwnerOrAdminPermission]
    #     return [permission() for permission in permission_classes]


# Generating a csrf token


# def get_csrf(request):
#     response = JsonResponse({"Info": " Success - set CSRF cookie"})
#     response["X-CSRFToken"] = get_token(request)
#     return response
