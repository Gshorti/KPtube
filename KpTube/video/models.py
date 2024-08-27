from django.db import models


# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    video = models.FileField(upload_to='videos/')
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
