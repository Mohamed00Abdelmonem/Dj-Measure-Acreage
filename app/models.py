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
    East_meter = models.FloatField()
    West_meter = models.FloatField()
    North_meter = models.FloatField()
    South_meter = models.FloatField()
    hypotenuse1 = models.FloatField(null=True, blank=True)
    hypotenuse2 = models.FloatField(null=True, blank=True)
    East = models.CharField(max_length=500)
    West = models.CharField(max_length=500)
    North  = models.CharField(max_length=500)
    South = models.CharField(max_length=500)
    area = models.CharField(max_length=500)
    price = models.FloatField()
    created_at = models.DateField(default=timezone.now)
    subtitle_information_for_land = models.TextField(null=True, blank=True, max_length=5000)
    image = models.ImageField(null=True, blank=True, upload_to='image_land')

    def __str__(self) -> str:
        return self.name_saler
    


class Data_For_Author(models.Model):
   price = models.FloatField()
   happy_or_not = models.BooleanField()
   created_at = models.DateField(default=timezone.now)
   defucalt = models.BooleanField()
   notes_for_me = models.TextField(null=True, blank=True, max_length=5000)
   who_with_me = models.CharField(null=True, blank=True, max_length=20, choices=WHO_WITH_ME)
   were_this_land = models.CharField(null=True, blank=True, max_length=500)
   Land = models.ForeignKey(Data_Land, related_name='auter_land', on_delete=models.SET_NULL, null=True)
   
   def __str__(self) -> str:
        return f"{self.price} - {self.Land}"


