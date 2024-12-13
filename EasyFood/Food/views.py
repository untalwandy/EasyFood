from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, View, CreateView, UpdateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.utils.decorators import method_decorator

from Company import models

from .models  import ConfigurationApp


class Dashboard(TemplateView):
      template_name = "food/dashboard.html"

      def get(self, request, *args, **kwargs):
            if not request.user.is_authenticated:
                  return redirect(reverse('company:logins'))

            if request.user.employee_profile.role == "estandar":
                   return redirect('company:no-acces-to-view')  
            return super().get(request, *args, **kwargs)    
            

      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['company'] = ''
            return context
    


    # Restaurante, Menu, Plato, Ingrediente, Categoria y Producto
class Restaurant(TemplateView):
      template_name = "food/restaurant/restaurant.html"

      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['platos'] = models.Plato.objects.all()
            context['categorias'] = models.Category.objects.all()
            return context



# Administracion, Proveedores, Clientes, Comisiones y Ventas
class Administration(TemplateView):
      template_name = "food/administration/administration.html"

      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return context



# Configuracion, Cambiar contraseña, Cambiar correo electronico y Mas
class Configuration(TemplateView):
      template_name = "food/configuration/configuration.html"

      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['configuration'] = ConfigurationApp.objects.get(id=1)
            return context

      def post(self, request, *args, **kwargs):
            configuration = ConfigurationApp.objects.get(id=1)
            print( request.POST.get('animations'))
            if request.POST.get('animations'):
                  if configuration.animations == True:
                        configuration.animations = False
                  else:
                        configuration.animations = True
                  configuration.save()
            return redirect(reverse('food:configuration'))
