from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from mainApp.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('main/', include('mainApp.urls')),
    path('order/', include('orderApp.urls')),
    path('user/', include('userApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
