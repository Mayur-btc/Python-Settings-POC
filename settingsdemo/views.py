from django.shortcuts import render,HttpResponse
from django.views import View

class Home(View):
    def get(self,request):
        return render(request,'settingsdemo/index.html')

