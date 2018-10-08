from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    minimumparticipant = models.PositiveIntegerField()
    maximumparticipant = models.PositiveIntegerField()
    date = models.CharField(max_length=20)
    entries = models.PositiveIntegerField()
    fees = models.PositiveIntegerField()
    user = models.ManyToManyField(User, null=True, blank=True)


    def __str__(self):
        return f'{self.name}'

class Sponser(models.Model):
    positive = models.IntegerField(default=1)
    negative = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    contact = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    final = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


