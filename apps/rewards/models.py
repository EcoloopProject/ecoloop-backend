from django.db import models

class Reward(models.Model):
    name = models.CharField(max_length=100)
    points_required = models.IntegerField()