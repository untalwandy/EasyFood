from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, View, CreateView, UpdateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.utils.decorators import method_decorator




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
    