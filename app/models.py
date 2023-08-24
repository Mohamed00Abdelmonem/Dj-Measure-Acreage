from django.db import models
from django.utils import timezone
# Create your models here.


WHO_WITH_ME = (
    ('Alone','Alone'),
    ('Abdelmonem','Abdelmonem'),
    ('Moahmed','Mohamed'),
)


class Data_Land(models.Model): 
    name_saler = models.CharField(max_length=100)
    name_buyer = models.CharField(max_length=100)
    hight = models.FloatField()
    width = models.FloatField()
    hypotenuse = models.FloatField()
    price = models.FloatField()
    created_at = models.DateField(default=timezone.now)
    subtitle_information_for_land = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='image_land')


class Data_For_Author(models.Model):
   price = models.FloatField()
   happy_or_not = models.BooleanField()
   created_at = models.DateField(default=timezone.now)
   defucalt = models.BooleanField()
   notes_for_me = models.TextField(max_length=5000)
   who_with_me = models.CharField(max_length=20, choices=WHO_WITH_ME)
   were_this_land = models.CharField(max_length=1000)
   

