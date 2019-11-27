from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import User
# Create your views here.
class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    fields = ['username', 'phone_number', 'gender',
              'birthday', 'image']