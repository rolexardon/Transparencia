from django.forms import ModelForm
from Administration.models import Usuario 
# Create the form class.
class UserForm(ModelForm):
     class Meta:
         model = Usuario