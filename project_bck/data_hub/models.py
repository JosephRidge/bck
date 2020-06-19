from django.db import models

# Create your models here.


class payload(models.Model):
    temperature = models.FloatField()
    heatindex_in_celsious = models.FloatField()
    heatindex_in_farenheit = models.FloatField()
    humidity = models.FloatField()
    temperature_celsius = models.FloatField()
    temperature_farenheit = models.FloatField()
    Ammonia = models.FloatField()
    carbon_dioxide = models.FloatField()
    carbon_monoxide = models.FloatField()
    sound_level = models.FloatField()

    def __str__(self):
        # return self.Ammonia, self.carbon_dioxide, self.temperature, self.heatindex_in_celsious, self.humidity, self.temperature_celsius, self.carbon_monoxide, self.sound_level
        return tuple("{:f} {:f} {:f} {:f} {:f} {:f} {:f} {:f} {:f} ".format(self.Ammonia, self.carbon_dioxide, self.temperature, self.heatindex_in_celsious, self.humidity, self.temperature_celsius, self.carbon_monoxide, self.sound_level)
                                                                      )
# eustin we have a problem, overload.