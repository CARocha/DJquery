from django.forms import ModelForm
from testjquery.models import Usuario
from django.forms.widgets import TextInput

class UsuarioForm(ModelForm):
	class Meta:
		model = Usuario
		fields = ('nombre', 'apellido', 'edad', 'twitter')
		widgets = {
            'nombre': TextInput(attrs={'class': 'required'}),
            'apellido': TextInput(attrs={'class': 'required'}),
            'edad': TextInput(attrs={'class': 'required'}),
            'twitter': TextInput(attrs={'class': 'required'}),
        }
