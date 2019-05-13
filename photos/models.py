from django.db import models


class Image(models.Model):
   image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
   image_name = models.CharField(max_length=100)
   image_description = models.TextField()

   def __str__(self):
       return self.image_name


class Location(models.Model):
   image = models.ForeignKey(Image, on_delete=models.CASCADE)
   image_location = models.CharField(max_length=100)

   def __str__(self):
       return self.image_location

class Category(models.Model):
   image = models.ForeignKey(Image, on_delete=models.CASCADE)
   image_category = models.CharField(max_length=100)

   def __str__(self):
       return self.image_category


