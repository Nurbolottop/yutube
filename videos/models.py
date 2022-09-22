from django.db import models
from users.models import User
# Create your models here.
class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
    related_name = "videos_user")
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to = "poster/")
    video_file = models.FileField(upload_to = "video/")
    created = models.DateField(auto_now_add=True)
