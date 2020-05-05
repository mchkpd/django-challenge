from django.db import models
from django.utils import timezone


class Activity(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField()
    factor = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Challenge(models.Model):
    name = models.CharField(max_length=64)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True)
    target = models.IntegerField()
    end_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField()
    tags = models.ManyToManyField(Tag, blank=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
