from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class ProfilAdmin(UserAdmin):
    fieldsets = [
        (None, {
            'fields': [
                'username',
                'password'
            ],
        }),
        ("Info", {
            'fields': [
                'first_name',
                'last_name',
                'phone_number',
                'gender',
                'country',
                'city',
                'confirmed'
            ],
        }),
    ]


admin.site.register(Profil, ProfilAdmin)

admin.site.register(
    [Country, City]
)
