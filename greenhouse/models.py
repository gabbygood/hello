from django.db import models

class Greenhouse(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='greenhouse_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
