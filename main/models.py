from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Game(models.Model):
    string = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
