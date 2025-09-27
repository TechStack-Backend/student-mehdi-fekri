from django.db import models



class Skill(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)  
    def __str__(self):
        return self.title
    

class Developer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name="Developer_skill"
    )
    def __str__(self):
        return self.first_name + self.last_name


