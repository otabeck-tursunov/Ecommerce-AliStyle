from django.shortcuts import render
from django.views import *

from .models import *


class Home(View):
    def get(self, request):
        categories = Category.objects.all()
        if request.user.is_authenticated:
            context = {
                'categories': categories
            }
            return render(request, 'home.html', context)
        return render(request, 'home-unauth.html')


class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        subCategories = SubCategory.objects.all()
        print('-----------------------------------------', categories.first().image.url)
        context = {
            'categories': categories,
            'subCategories': subCategories
        }
        return render(request, 'categories.html', context)


class SubCategoriesView(View):
    def get(self, request):
        subCategories = []
        context = {
            'subCategories': subCategories
        }
        return render(request, 'subCategories.html', context)


class ProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        if request.GET.get('category_id'):
            products = products.filter(category__id=request.GET.get('category_id'))
        context = {
            'products': products
        }
        return render(request, 'products.html', context)


class ProductView(View):
    def get(self, request, pk):
        product = "Salom"
        context = {
            'product': product
        }
        return render(request, 'product.html', context)
