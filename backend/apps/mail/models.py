from django.db import models
from django.utils import timezone

from apps.accounts.models import User

class Mail(models.Model):
     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
     message = models.CharField(max_length=1200)
     timestamp = models.DateTimeField(auto_now_add=True)

     def __str__(self):
           return self.message

     class Meta:
           ordering = ('timestamp',)
