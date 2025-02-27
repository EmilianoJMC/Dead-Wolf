from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=100)

class Music(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, related_name='musics', on_delete=models.CASCADE)
    file = models.FileField(upload_to='musics/', blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)