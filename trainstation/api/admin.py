from django.contrib import admin

from .models import Train, TrainSection, Person

admin.site.register([Train, TrainSection, Person])
