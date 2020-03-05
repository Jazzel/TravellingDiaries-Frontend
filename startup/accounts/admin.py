from django.contrib import admin
from .models import UserProfile, UserLog, Address
# Register your models here.

admin.site.site_header = "TravellingDiaries"


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']


admin.site.register(UserProfile)
admin.site.register(UserLog)
admin.site.register(Address, AddressAdmin)
