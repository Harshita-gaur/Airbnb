# Create your models here.
from django.db import models

class AirbnbListing(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price_per_night = models.FloatField()
    ratings = models.FloatField(null=True, blank=True)
    reviews = models.CharField(max_length=255,blank=True,default="1")
    amenities = models.CharField(max_length=255,blank=True)
    image = models.ImageField(upload_to='listings/', default='default.png')


    def __str__(self):
            return self.title

