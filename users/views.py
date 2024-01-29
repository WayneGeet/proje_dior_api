# from .serializers import UserLoginSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
# from django.contrib.auth import login, logout
from .serializers import UserSerializer
from .models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth import get_user_model
from django.http import Http404
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect


User = get_user_model()


class IsOwnerOrAdminPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the object or an admin
        # print(f"{request.user} and {request.auth}")
        return obj == request.user or request.user.is_staff


# @method_decorator(csrf_protect, name="dispatch")
class UserList(APIView):
    permission_classes = (IsAdminUser,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        data = User.objects.all()
        serializer = UserSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):
    permission_classes = (IsOwnerOrAdminPermission,)
    authentication_classes = (JWTAuthentication,)

    def get_object(self, slug=None):
        try:
            return User.objects.get(slug=slug)
        except User.DoesNotExist:
            raise Http404

    def put(self, request, slug=None, format=None):
        user = self.get_object(slug)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug=None):
        user = self.get_object(slug)
        if user:
            user.delete()
            return Response({"message": "user delete succesful"}, status=status.HTTP_200_OK)
        return Response({"message": "user with that id does not exist"}, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (JWTAuthentication,)

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data, many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserLoginView(APIView):
#     permission_classes = (AllowAny,)
#     authentication_classes = (JWTAuthentication,)

#     def post(self, request):
#         credentials = request.data
#         serializer = UserLoginSerializer(data=credentials, many=False)
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.check_user(credentials)
#             login(request, user)
#             return Response(serializer.data, status=status.HTTP_200_OK)


# class UserLogoutView(APIView):
#     def post(self, request):
#         logout(request)
#         Response({"message": "user logged out successfully"},
#                  status=status.HTTP_200_OK)


class UserView(APIView):
    permission_classes = (IsOwnerOrAdminPermission,)

    def get(self, request):
        user = request.user
        print(f"{user} this is me")
        if (user is not None):
            # Use 'instance=user' instead of 'data=user'
            serializer = UserSerializer(instance=user)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "unauthorized access"}, status=status.HTTP_401_UNAUTHORIZED)
