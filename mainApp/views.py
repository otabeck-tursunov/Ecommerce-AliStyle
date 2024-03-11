from django.shortcuts import render
from django.views import *


class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'index-main.html')
        return render(request, 'index-without-login.html')
