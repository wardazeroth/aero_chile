"""
URL configuration for citas_medicas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import inicio, RegistroView, VueloView, PasajeroView, detalle_vuelo, completar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registro', RegistroView.as_view(), name='registro'),
    path('', inicio, name='inicio'),
    path('flights/new', VueloView.as_view(), name= 'nuevo_vuelo'),
    path('flights/<codigo>/newpassenger', PasajeroView.as_view(), name= 'nuevo_pasajero'),
    path('flights/<codigo>', detalle_vuelo, name = 'detalle_vuelo'),
    path('<codigo>', completar, name='completar')
    # path('notas', NotaView.as_view(), name='nueva_nota'),
]
