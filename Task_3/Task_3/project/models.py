from django.db import models
from developers.models import Developer
# Create your models here.
class project(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    developers = models.ManyToManyField(Developer,related_name="projects")
    def __str__(self):
        return self.title