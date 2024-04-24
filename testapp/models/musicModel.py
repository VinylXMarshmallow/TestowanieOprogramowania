from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=100,default='')
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True)
    popular = models.IntegerField(default=0)

    def __str__(self):
        return self.title
