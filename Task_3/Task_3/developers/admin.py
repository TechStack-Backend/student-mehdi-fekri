from django.contrib import admin
from .models import Developer

class Developer_admin(admin.ModelAdmin):
    list_display= ("first_name","last_name","email","skill")

admin.site.register(Developer, Developer_admin)

class Skills_admin(admin.ModelAdmin):
    list_display= ("title","description")

