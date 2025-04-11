from django.contrib import admin
from .models import TaskList,Task,CountryList

admin.site.register(TaskList)
admin.site.register(Task)
admin.site.register(CountryList)


