from django.db import models

class Noun(models.Model):
    polish = models.CharField(max_length=255)
    spanish = models.CharField(max_length=255)
