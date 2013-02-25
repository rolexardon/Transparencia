from django.forms import ModelForm
from Transparencia.Administration.models import Usuario
from django.contrib.auth.models import User

        
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        exclude = ('is_staff','is_active','is_superuser','last_login','date_joined','groups','user_permissions')
        
    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.email = self.cleaned_data["email"]
        user.is_active = True
        if commit:
            user.save()
        return user
    
class UsuarioModForm(ModelForm):
	class Meta:
		model = Usuario
		exclude = ('is_staff','is_active','is_superuser','last_login','date_joined','groups','user_permissions','password')
		
