from rest_framework.views import APIView
from rest_framework.response import Response
from apps.users.models import User


class LeaderboardView(APIView):
    def get(self, request):
        # 🔥 get top 10 users sorted by points
        users = User.objects.order_by('-points')[:10]

        data = []
        for i, u in enumerate(users):
            data.append({
                "name": u.username,
                "points": u.points,
                "rank": i + 1,  # 🏆 rank (use later in frontend)
                "isCurrentUser": (
                    request.user.is_authenticated and u == request.user
                )  # 🔐 safe check
            })

        return Response(data)