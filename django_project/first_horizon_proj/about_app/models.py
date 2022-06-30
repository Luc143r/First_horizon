from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title