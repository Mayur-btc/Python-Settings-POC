from django.shortcuts import render,HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginRequiredMixin,View):
    def get(self,request):
        user = {'name':request.user}
        print(request.user,request.user.id)
        return render(request,'settingsdemo/index.html',context={'user':request.user})

