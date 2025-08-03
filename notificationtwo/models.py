from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Notification(models.Model):
    NOTIF_TYPE_CHOICES = [
        ('reminder', 'Reminder'),
        ('alert', 'Alert'),
        ('water', 'Watering'),
        ('harvest', 'Harvest'),
    ]

    # 👇 Renamed related_name to avoid clash with other apps
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_notifications'
    )

    sender = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sent_notifications'
    )

    notif_type = models.CharField(max_length=20, choices=NOTIF_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} → {self.user}"
