from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('subCategories/', SubCategoriesView.as_view(), name='subCategories'),
    path('products/', ProductsView.as_view(), name='products'),
    path('products/<int:pk>/', ProductView.as_view(), name='product'),
]