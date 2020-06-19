from django.db import models


class device(models.Model):
    device_id = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    battery_status = models.FloatField()

    def __str__(self):
        return self.device_id
