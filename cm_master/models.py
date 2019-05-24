from django.db import models
from django.utils.translation import ugettext as _


class SpeedDetector(models.Model):
    c_id = models.BigAutoField(primary_key=True)
    car_speed = models.IntegerField(default=0)
    speed_limit = models.IntegerField(default=0)
    location = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=100, null=True, blank=True)
    date_captured = models.DateTimeField(null=True, blank=True)
    car = models.FileField(upload_to='documents/%Y/%m/%d', null=True, blank=True)
    test_id = models.CharField(null=True, blank=True, max_length=10000)

    class Meta:
        verbose_name = _("Speed Detector")
        verbose_name_plural = _("Speed Detector")
        db_table = "speed_detector"

    def __str__(self):
        return str(self.c_id)

    def __int__(self):
        return self.c_id
