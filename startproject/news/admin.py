# Register your models here.
from django.contrib import admin

from .models import Category, Tag, News

admin.site.register([Category, Tag, News])