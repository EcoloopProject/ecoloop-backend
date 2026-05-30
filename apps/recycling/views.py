from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Recycling

class SubmitRecycling(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        quantity = int(request.data['quantity'])

        Recycling.objects.create(
            user=request.user,
            waste_type=request.data['waste_type'],
            quantity=quantity
        )

        request.user.points += quantity * 10
        request.user.save()

        return Response({
            "message": "Submitted",
            "points": request.user.points
        })