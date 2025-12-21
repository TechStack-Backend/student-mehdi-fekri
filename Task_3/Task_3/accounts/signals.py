from . import models
from django.db.models.signals import post_save , pre_save
from .models import Profile
from django.dispatch import receiver
from django.contrib.auth.models import User,Group

def User_post_save(sender,instance,created,*args, **kwargs):
    print('post_save signal called')
    # print(sender,instance)
    if created:
        Profile.objects.get_or_create(user =instance)
        developer_group = Group.objects.filter(name='Developer').first()        
        instance.groups.add(developer_group)


post_save.connect(User_post_save,sender=User)



# def User_pre_save(sender,instance,*args, **kwargs):
#      print('pre_save signal called')
#      print(sender,instance)
# pre_save.connect(User_pre_save,sender=Profile)