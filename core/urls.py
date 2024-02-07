from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from projects.views import ProjectModelViewSet
from users.views import UserModelViewSet
from rest_framework import routers
from user_profile.views import ProfileModelViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r"projects", ProjectModelViewSet)
router.register(r'users', UserModelViewSet)
router.register(r'profiles', ProfileModelViewSet, basename='profile')

urlpatterns = [
    # path('projects/<int:pk>/like/', ToggleLikeView.as_view(), name='toggle_like'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("", include(router.urls)),
    # path("accounts/csrf/", get_csrf, name="csrf-token"),
    # user views
    # path("users/register/", userview.UserRegisterView.as_view()),
    # path("users/login/", userview.UserLoginView.as_view()),
    # path("users/logout/", userview.UserLogoutView.as_view()),
    # path("users/", userview.UserList.as_view()),
    # path("users/<slug:slug>/", userview.UserDetails.as_view()),
    # path("user/me/", userview.UserView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('users/profiles/<slug:slug>/',
    #      ProfileDetails.as_view(), name='profile-detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
