# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
 class Profile(models.Model):
    dpic = models.ImageField(upload_to = 'images/')
    bio = models.TextField(max_length=1000)
    info = models.TextField(max_length=5000)

    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Projects(models.Model):
    title = models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    link=models.URLField()
    image=models.ImageField(upload_to='images/')
    user = models.ForeignKey(User,on_delete = models.CASCADE)


    def save_project(self):
        self.save()

    @classmethod
    def all_projects(cls):
    
    all_projects = cls.objects.all()
        return all_projects