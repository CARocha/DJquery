from django.forms import ModelForm
from testjquery.models import Usuario

class UsuarioForm(ModelForm):
	class Meta:
		model = Usuario