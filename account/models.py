from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile (models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,blank=False,null=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    email=models.CharField(max_length=200)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"{self.username} {self.pk}"



