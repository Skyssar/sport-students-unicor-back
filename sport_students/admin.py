from django.contrib import admin
from .models import Profile, Sport, SportHistoryInfo, SportHistory, PhysicalInfo

# Register your models here.
admin.site.register( Profile )
admin.site.register( PhysicalInfo )
admin.site.register( Sport )
admin.site.register( SportHistoryInfo )
admin.site.register( SportHistory )