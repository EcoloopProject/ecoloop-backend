from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Recycling(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    waste_type = models.CharField(max_length=100)
    quantity = models.FloatField()
    status = models.CharField(default="pending", max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)