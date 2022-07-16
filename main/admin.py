from django.contrib import admin

from .models import Task

# Register your models here.
# pass = todo1234
admin.site.register(Task)