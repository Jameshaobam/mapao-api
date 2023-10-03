"""
URL configuration for mapao_test project.

"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/account/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/',include('discover.urls')),
    path('api/v1/account/',include('account.urls')),
    path('api/v1/event/',include('event.urls')),
    path('api/v1/feed/',include('feed.urls')),
]
