from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class TrainSection(models.Model):
    name = models.CharField(max_length=30)


class Train(models.Model):
    name = models.CharField(max_length=30)


class Platform(models.Model):
    name = models.CharField(max_length=30)


class TrainStation(models.Model):
    name = models.CharField(max_length=30)
