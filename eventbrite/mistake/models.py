from django.db import models

# Create your models here.
from django.db import models
class Event(models.Model):
    event_id = models.AutoField
    date = models.DateField()
    time = models.TimeField()
    vname = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=100, default="")
    img = models.ImageField(upload_to="mistake/images", default="" )

    def __str__(self):
        return self.vname