from django.shortcuts import render
from django.views import View

from AliStyle import settings


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')


class ConfirmView(View):
    def get(self, request):
        return render(request, 'confirm.html')
