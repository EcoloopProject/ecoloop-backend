from rest_framework.views import APIView
from rest_framework.response import Response
from apps.users.models import User

class LeaderboardView(APIView):
    def get(self, request):
        users = User.objects.order_by('-points')[:10]
        return Response([
            {"username": u.username, "points": u.points}
            for u in users
        ])