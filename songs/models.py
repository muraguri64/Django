from django.db import models

# Create your models here.

class Song(models.Model):
	album = models.IntegerField()
	song_title = models.CharField(max_length=250)
	file_type = models.CharField(max_length=10)

def __str__(self):
        return self.album + ' - ' + self.song_title