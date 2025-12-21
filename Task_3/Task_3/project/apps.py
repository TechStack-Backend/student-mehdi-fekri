from django.apps import AppConfig
from django.db.models.signals import post_migrate,pre_save
def create_default_group(sender,**kwargs):
    from django.contrib.auth.models import Group
    groups = ['Admin','Manager','Developer']
    for name in groups:
        group , created =Group.objects.get_or_create(name=name)
        if created:
            print(f"{name} created for first")
    print("--- Project Groups Created Successfully ---")



def User_pre_save(sender,instance,*args, **kwargs):
    instance.title = "Project_"+instance.title
    #  print('pre_save signal called')
    #  print(sender,instance)
    print(instance.title)



class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project'

    def ready(self):
        post_migrate.connect(create_default_group,sender=self)
        from .models import project
        pre_save.connect(User_pre_save,sender=project)
