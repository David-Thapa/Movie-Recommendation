from django.db import models

# Create your models here.

class Movie(models.Model):
    tmdb_id = models.CharField(max_length=20, primary_key=True)
    imdb_id = models.CharField(max_length=50)
    original_language = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
#    poster_path = models.CharField(max_length=255)
    # release_date = models.DateField()
    runtime = models.IntegerField()

    def __str__(self):
        return self.original_title

    class Meta:
        ordering = ['original_title']