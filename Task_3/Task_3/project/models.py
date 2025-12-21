from django.db import models
from developers.models import Developer
from django.contrib.auth.models import User
class project(models.Model):
    is_approved = models.BooleanField(default=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='project',null=True,blank=True)
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    developers = models.ManyToManyField(Developer,related_name="projects")
    class Meta:
        permissions = [
            ("can_assign_developers", "Can assign developers to a project"),
        ]
    def __str__(self):
        return self.title