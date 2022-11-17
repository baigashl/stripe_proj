from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
