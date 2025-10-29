from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    RegisterView,
    LoginView,
    UserProfileView,
    LogoutAndBlacklistRefreshTokenView,
)

urlpatterns = [
    # -------------------------
    # Custom user endpoints
    # -------------------------
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutAndBlacklistRefreshTokenView.as_view(), name='logout'),

    # -------------------------
    # Built-in JWT endpoints (SimpleJWT)
    # -------------------------
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
