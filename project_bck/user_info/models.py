from django.db import models


class user(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.first_name

