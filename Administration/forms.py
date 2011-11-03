from django.forms import ModelForm
from Administration.models import Usuario, TipoUsuario, Rol 
# Create the form class.
class UserForm(ModelForm):
     class Meta:
         model = Usuario
class TiposForm(ModelForm):
     class Meta:
         model = TipoUsuario
class RolesForm(ModelForm):
     class Meta:
         model = Rol