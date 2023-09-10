from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    # overrides the admin panel and display it this way
    list_display = ('task','is_completed','updated_at')
    # shows the search field in the admin panel
    search_fields = ('task',)

admin.site.register(Task,TaskAdmin)
