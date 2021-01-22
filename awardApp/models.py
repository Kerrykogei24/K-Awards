# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
 class Profile(models.Model):
    dpic = models.ImageField(upload_to = 'images/')
    bio = models.TextField(max_length=1000)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

        