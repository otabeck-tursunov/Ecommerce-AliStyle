from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import *
import random
from eskiz.client import SMSClient
from django.contrib.auth import authenticate, login, logout

from AliStyle import settings


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        profil = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        print(profil)
        if profil is not None:
            if profil.confirmed:
                login(request, profil)
                print("login boldi")
                return redirect('home')
            return redirect('confirm')
        return redirect('login')


class RegisterView(View):
    def get(self, request):
        countryies = Country.objects.all()
        cities = City.objects.all()
        context = {
            'countryies': countryies,
            'cities': cities
        }
        return render(request, 'register.html', context)

    def post(self, request):
        if request.POST.get('password1') != request.POST.get('password2'):
            return HttpResponse('Passwordlar bir xil emas!')
        profil = Profil.objects.create_user(
            username=request.POST['phone_number'],
            password=request.POST['password1'],
            phone_number=request.POST['phone_number'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            country=Country.objects.get(id=request.POST['country']),
            city=City.objects.get(id=request.POST['city']),
            gender=request.POST['gender'],
            confirmation_code=str(random.randrange(111111, 999999))
        )
        client = SMSClient(
            api_url="https://notify.eskiz.uz/api/",
            email="tursunovotabekkuva@gmail.com",
            password=settings.ESKIZ_TOKEN,
        )
        client._send_sms(
            phone_number=profil.phone_number,
            message=f'AliStyle Online do\'koniga ro\'yxatdan o\'tish uchun tasdiqlash kodi: {profil.confirmation_code}'
        )
        login(request, profil)
        return redirect('confirm')


class ConfirmView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'confirm.html')
        return redirect('login')

    def post(self, request):
        profil = Profil.objects.get(id=request.user.id)
        if profil.confirmation_code == request.POST['confirmation_code']:
            profil.confirmed = True
            profil.save()
            logout(request)
            return redirect('login')
        return redirect('confirm')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
