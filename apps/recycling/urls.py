from django.urls import path
from .views import SubmitRecycling

urlpatterns = [
    path('submit/', SubmitRecycling.as_view()),
]