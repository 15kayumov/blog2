from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(blank=True)
    text = models.TextField( )
    title2=models.CharField(max_length=200)
    text2 = models.TextField()


    def str(self):
        return self.title