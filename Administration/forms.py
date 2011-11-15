from django.forms import ModelForm
from Administration.models import Usuario, TipoUsuario, Rol
from django.contrib.auth.models import User 
# Create the form class.
class UserForm(ModelForm):
     class Meta:
         model = User
         exclude = ("user_permissions","is_staff","superuser","groups","last_login","is_superuser","date_joined")
class ProfileUserForm(ModelForm):
     class Meta:
         model = Usuario
         exclude = ("user")
class TiposForm(ModelForm):
     class Meta:
         model = TipoUsuario
class RolesForm(ModelForm):
     class Meta:
         model = Rol