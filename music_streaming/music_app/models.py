from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=255)

class Music(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, related_name='musics', on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)