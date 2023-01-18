from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=500, default='')
    url = models.CharField(max_length=200, default='')
    duration = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title