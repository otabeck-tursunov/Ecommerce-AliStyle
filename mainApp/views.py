from django.shortcuts import render
from django.views import *

from mainApp.models import *


class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'index-main.html')
        return render(request, 'index-without-login.html')


class Categories(View):
    def get(self, request):
        categories = Category.objects.all()
        subCategories = SubCategory.objects.all()
        print('-----------------------------------------', categories.first().image.url)
        context = {
            'categories': categories,
            'subCategories': subCategories
        }
        return render(request, 'categories.html', context)


class SubCategories(View):
    def get(self, request):
        subCategories = []
        context = {
            'subCategories': subCategories
        }
        return render(request, 'subCategories.html', context)


class Products(View):
    def get(self, request):
        products = []
        context = {
            'products': products
        }
        return render(request, 'products.html', context)


class Product(View):
    def get(self, request, pk):
        product = "Salom"
        context = {
            'product': product
        }
        return render(request, 'product.html', context)
