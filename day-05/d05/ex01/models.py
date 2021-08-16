from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField('Title', max_length=64, null=False, unique=True)
    episode_nb = models.IntegerField('Episode number', primary_key=True)
    opening_crawl = models.TextField('Opening crawl', null=True)
    director = models.CharField('Director', max_length=32, null=False)
    producer = models.CharField('Producer', max_length=128, null=False)
    release_date = models.DateField('Release date', null=False)

    def __str__(self):
        return self.title