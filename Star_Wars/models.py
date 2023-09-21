from django.db import models
from django import forms


class Character(models.Model):
    options = (
        ("empire", "Empire"),
        ("rebellion", "Rebellion"),
    )

    name = models.CharField(max_length=40)
    species = models.CharField(max_length=20)
    movie = models.CharField(max_length=40)
    side = models.CharField(max_length=20, choices=options)
    objects = models.Manager()

    def __str__(self):
        return self.name


