from django.shortcuts import render, redirect
from matery.models import matery
from user.mixins import LoginYSuperStaffMixin
from django.views.generic import CreateView
from matery.forms import FormMatery
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from user.mixins import LoginYSuperStaffMixin

# Create your views here.

class añadirMateria(PermissionRequiredMixin,CreateView):
	model = matery
	form_class = FormMatery
	template_name = 'matery/matery.html'
	success_url = reverse_lazy('home')
	permission_required = {'materia.permiso_admin'}