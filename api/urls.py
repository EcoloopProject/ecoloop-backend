from django.urls import path, include

urlpatterns = [
    path('auth/', include('apps.users.urls')),
    path('recycling/', include('apps.recycling.urls')),
    path('rewards/', include('apps.rewards.urls')),
    path('leaderboard/', include('apps.leaderboard.urls')),
]