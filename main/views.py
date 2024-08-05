from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test, login_required
from main.models import Viaje, Avion
from main.forms import ViajeModelForm, PasajeroModelForm

# Vista abierta a todo público
def inicio(req):

  vuelos = Viaje.objects.all()
  context = {
    'vuelos': vuelos
  }
  return render(req, 'index.html', context)

# ClassView abierta
class RegistroView(View):

  def get(self, req):
    return render(req, 'registration/registro.html')
  
  def post(self, req):
    # 1. Recuperamos los datos del formulario
    username = req.POST['username']
    email = req.POST['email']
    password = req.POST['password']
    pass_repeat = req.POST['pass_repeat']
#     pass_repeat = req.POST['pass_repeat']
    # 2. Validamos que contraseñas concidan
    if password != pass_repeat:
      messages.error(req, 'Contraseñas no coinciden')
      return redirect('/accounts/registro')
    # 3. Creamos al usuario
    User.objects.create_user(username=username, email=email, password=password)
    # 5. Feedback y redirigimos
    messages.success(req, 'Usuario creado')
    return redirect('/')
  
def nuevo_vuelo(req):
  return render(req, 'nuevo_vuelo.html')

class VueloView(View):
  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
      return super().dispatch(*args, **kwargs)
  
  def get(self, req):
    form = ViajeModelForm()
    aviones = Avion.objects.raw("""
            select * from main_avion
            where id not in (
              select avion_id from main_viaje where estado = 'agendado' 
            )
        """) 
    context = {
      'form': form,
      'aviones': aviones
    }
    return render(req, 'nuevo_vuelo.html', context)
  
  def post(self, req):
    
    form = ViajeModelForm(req.POST)
    viaje = form.save()
    viaje.estado = 'agendado'
    viaje.save()
    messages.success(req, 'Vuelo Creado')
    return redirect('/')
    
class PasajeroView(View):
  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)
  def get(self, req, codigo):
    codigo = Viaje.objects.get(codigo=codigo)
    form = PasajeroModelForm()
    context = {
      'form': form
      }
    return render(req, 'nuevo_pasajero.html', context)
  
  def post(self, req, codigo):
    viaje = Viaje.objects.get(codigo=codigo)
    form = PasajeroModelForm(req.POST)
    pasajero = form.save(commit=False)
    pasajero.viaje = viaje
    pasajero.save()
    messages.success(req, 'Pasajero agregado')
    return redirect('/')

    
# def nuevo_pasajero(req, codigo):
#   codigo = Viaje.objects.get(codigo=codigo)
#   form = PasajeroModelForm()
  
#   context = {
#     'codigo': codigo,
#     'form': form
#   }
#   return render(req, 'nuevo_pasajero.html', context)

def detalle_vuelo(req, codigo):
  detalle = Viaje.objects.get(codigo=codigo)
  pasajeros = detalle.pasajeros.all()
  
  context = {
    'detalle': detalle,
    'pasajeros': pasajeros
  }
  return render(req, 'ver_detalle.html', context)
  
def completar(req, codigo):
  viaje = Viaje.objects.get(codigo=codigo)
 
  viaje.estado = 'completado'
  actual = viaje.destino
  viaje.avion.ciudad_actual = actual
  viaje.avion.save()
  viaje.save()
  messages.success(req, 'Vuelo Completado')
  return redirect('/')
  
