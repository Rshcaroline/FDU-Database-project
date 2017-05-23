from django.contrib import admin

from .models import appoint_acm, appoint_station, appoint_lecture, Acm, Station, Lecture

# Register your models here.

admin.site.register([appoint_acm, appoint_station, appoint_lecture, Acm, Station, Lecture])