from django.contrib import admin
from .models import User, Event,Sponser
# Register your models here.

admin.site.register(Event)
admin.site.register(Sponser)