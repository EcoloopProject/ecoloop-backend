from django.urls import path
from .views import RewardList

urlpatterns = [
    path('', RewardList.as_view()),
]