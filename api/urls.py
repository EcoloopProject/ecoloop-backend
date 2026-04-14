from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('auth/', include('apps.users.urls')),
    path('recycling/', include('apps.recycling.urls')),
    path('rewards/', include('apps.rewards.urls')),
    path('leaderboard/', include('apps.leaderboard.urls')),

    # 🔐 LOGIN API
    path('login/', TokenObtainPairView.as_view(), name='login'),
]