from django.contrib import admin
from . import models


class SpeedDetectorAdmin(admin.ModelAdmin):
    list_per_page = 1000
    show_full_result_count = False
    list_display = [f.name for f in models.SpeedDetector._meta.fields]


admin.site.register(models.SpeedDetector, SpeedDetectorAdmin)
