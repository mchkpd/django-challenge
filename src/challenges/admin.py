from django.contrib import admin

from .models import Activity
from .models import Tag
from .models import Challenge

admin.site.register(Activity)
admin.site.register(Tag)
admin.site.register(Challenge)
