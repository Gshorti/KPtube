from django.db import models


# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.name
