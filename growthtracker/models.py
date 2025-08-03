from django.conf import settings
from django.db import models

class PlantGrowthEvent(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='growth_events'
    )
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.date} - {self.description}"
