from django.db import models


class TrainStation(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Train(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=30)
    train = models.ForeignKey(Train, on_delete=models.SET_NULL)
    station = models.ForeignKey(TrainStation, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class TrainSection(models.Model):
    name = models.CharField(max_length=30)
    train = models.ForeignKey(Train, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    train_section = models.ForeignKey(TrainSection, on_delete=models.PROTECT)

    def __str__(self):
        return self.full_name
