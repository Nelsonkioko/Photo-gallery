from django.db import models


class Location(models.Model):
    image_location = models.CharField(max_length=100)

    def __str__(self):
        return self.image_location


class Category(models.Model):
    image_category = models.CharField(max_length=100)

    def __str__(self):
        return self.image_category


class Image(models.Model):
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    image_name = models.CharField(max_length=100)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name
