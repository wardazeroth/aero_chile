from django import forms
from django.forms import ModelForm
from main.models import Viaje, Pasajero

class ViajeModelForm(ModelForm):
  class Meta:
    model = Viaje
    fields = ['codigo', 'origen', 'fecha', 'destino', 'avion']
    
    widgets = {
      'codigo': forms.TextInput(
        attrs= {
          'class': 'form-control',
          'type': 'text'
        }
      ),
      
      'origen': forms.Select(
        attrs={
          'class': 'form-select'
        }
      ),

      'fecha': forms.DateInput(
        attrs={
          'class':'form-control',
          'type':'date'
        }
      ),
      'destino': forms.Select(
        attrs={
          'class':'form-select',
        }
      ),

      # 'avion': forms.Select(
      #   attrs={
      #     'class': 'form-select'
      #   }
      # )     
    }

class PasajeroModelForm(ModelForm):
  class Meta:
    model = Pasajero
    fields = ['nombre', 'fecha_nacimiento', 'vacuna', 'rut']
    
    widgets = {
        'nombre': forms.TextInput(
      attrs= {
        'class': 'form-control',
        'type': 'text'
      }
    ),
        
              'fecha_nacimiento': forms.DateInput(
          attrs={
            'class':'form-control',
            'type':'date'
          }
        ),
      

    'vacuna': forms.Select(
      attrs={
        'class': 'form-select'
      }
    ),   
        'rut': forms.TextInput(
      attrs= {
        'class': 'form-control',
        'type': 'text'
      }
    )
    
  }
        
        