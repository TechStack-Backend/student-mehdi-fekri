from django.contrib.auth.mixins import AccessMixin
#Access mixin used for if user not authenrised so redirist user to login page 
#or if he authurised but not permission redirect user to 403 error page 
#and with this mixin i must`t implement has_no_permission and this mixix base of 
# Login or permission required mixins.
from django.core.exceptions import PermissionDenied
class OwnerOrPermissionMixin():
    required_permission = None
    owner_filed = 'owner'
    def dispatch(self,request, *args, **kwargs):
        obj = self.get_object()
        is_owner = getattr(obj,self.owner_filed) == request.user
        has_perm = request.user.has_perm(self.required_permission) if self.required_permission else False

        if not (is_owner or has_perm):
             raise PermissionDenied
        
        return super().dispatch(request,*args, **kwargs)
