"""
URL configuration for onboarding project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # Login endpoint - get access & refresh tokens
    TokenRefreshView,      # Refresh endpoint - get new access token
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # ============= JWT AUTHENTICATION ENDPOINTS =============
    # HOW TO USE:
    # 1. LOGIN (Get Tokens):
    #    POST /api/token/
    #    Body: {"username": "admin", "password": "password"}
    #    Returns: {"access": "<token>", "refresh": "<token>"}
    #
    # 2. REFRESH TOKEN (Get New Access Token):
    #    POST /api/token/refresh/
    #    Body: {"refresh": "<refresh_token>"}
    #    Returns: {"access": "<new_access_token>", "refresh": "<new_refresh_token>"}
    #
    # 3. USE TOKEN (Access Protected API):
    #    GET /api/employees/
    #    Headers: Authorization: Bearer <access_token>

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # when i send a post request to this url with username and password it will return access and refresh tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # when i send a post request to this url with refresh token it will return new access token

    # ============= API ENDPOINTS =============
    path('api/', include('tasks_app.urls')),
]
