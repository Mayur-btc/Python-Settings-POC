from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import User
from django.contrib.auth import authenticate,login
# Create your views here.
class UserCreateView(CreateView):
    model = User
    fields = ['username','password', 'phone_number', 'gender', 'birthday', 'image']
    def form_valid(self, form):
        user = super().form_valid(form)
        self.object.set_password(form.cleaned_data['password'])
        self.object.save()
        login(self.request, self.object)
        return user
        