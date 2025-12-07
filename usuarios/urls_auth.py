from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .token_views import EmailTokenObtainPairView

urlpatterns = [
    path("login/", EmailTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
