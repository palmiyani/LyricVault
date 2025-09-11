from django.db import models

class Song(models.Model):
    song_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    releasedate = models.DateField()
    url = models.URLField()
    views = models.IntegerField()

    def __str__(self):
        return self.song_name
