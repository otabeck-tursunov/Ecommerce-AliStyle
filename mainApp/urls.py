from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', Categories.as_view(), name='categories'),
    path('subCategories/', SubCategories.as_view(), name='subCategories'),
    path('products/', Products.as_view(), name='products'),
    path('products/<int:pk>/', Product.as_view(), name='product'),

]