from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    ratings = models.FloatField()
    release_date = models.DateField()
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    