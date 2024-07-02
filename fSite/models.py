
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.contrib import admin
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='profile_images/', default='juju.jpg')
    about = models.TextField(blank=True)
    reviews = models.IntegerField(default=0)
    created_on = models.DateTimeField(default=timezone.now)
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        output_size = (200, 200)
        img.thumbnail(output_size)
        img.save(self.image.path)


class Restaraunt(models.Model):
    subname = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    phone = PhoneNumberField()
    url = models.URLField(blank=True)
    openhours = models.CharField(max_length=15, blank=True)
    stars = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=100, blank=True)
    avgcheck = models.IntegerField(default=-1)
    image1 = models.ImageField(upload_to='restaurant_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='restaurant_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='restaurant_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='restaurant_images/', blank=True, null=True)

    @property
    def number_of_comments(self):
        return Comment.objects.filter(blogpost_connected=self).count()


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    rest_connected = models.ForeignKey(
        Restaraunt, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author) + ', ' + self.rest_connected.title[:40]


