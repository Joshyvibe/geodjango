from django.contrib.gis.db import models


class UserLocation(models.Model):
    location = models.PointField()


    def __str__(self):
        return f"Location: {self.location}"

    
