from django.contrib import admin

from .models import ClickCount, Stuff

admin.site.register(ClickCount)
admin.site.register(Stuff)

