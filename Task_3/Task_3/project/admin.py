from django.contrib import admin
from .models import project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "get_developers")

    def get_developers(self, obj):
        return ", ".join([dev.first_name + " " + dev.last_name for dev in obj.developers.all()])

    get_developers.short_description = "Developers"

admin.site.register(project, ProjectAdmin)
