from django.contrib import admin
from django.db import models

from django.shortcuts import render



class Contact(models.Model):
    name = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=1000)


