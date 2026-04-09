from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Reward

class RewardList(APIView):
    def get(self, request):
        rewards = Reward.objects.all().values()
        return Response(rewards)