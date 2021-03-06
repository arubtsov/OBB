from django.db import models


class NamedEntity(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class TrainStation(NamedEntity):
    pass


class Train(NamedEntity):    
    def get_passengers(self):
        passengers = []

        for section in self.sections.all().prefetch_related('passengers'):
            passengers.extend(section.passengers.all())

        return passengers



class Platform(NamedEntity):
    train = models.OneToOneField(Train, null=True, on_delete=models.SET_NULL)
    station = models.ForeignKey(TrainStation, on_delete=models.CASCADE)


class TrainSection(NamedEntity):
    train = models.ForeignKey(Train, on_delete=models.PROTECT, related_name='sections')
    order = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['train', 'order'], name='unique_section_position')
        ]


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    train_section = models.ForeignKey(TrainSection, null=True, blank=True, on_delete=models.PROTECT, related_name='passengers')

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
