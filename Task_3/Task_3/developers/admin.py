from django.contrib import admin
from .models import Developer,Skill

class Developer_admin(admin.ModelAdmin):
    # list_display= ("first_name","last_name","email","skill")
    list_display= ("first_name","last_name","email","skill_display")
    def skill_display(sself,obj):
        return ",".join([s.title for s in obj.skill.all()])
    #skill_display.short_description = "Skills"
   
admin.site.register(Developer, Developer_admin)

class Skills_admin(admin.ModelAdmin):
    list_display= ("title","description")

admin.site.register(Skill, Skills_admin)
