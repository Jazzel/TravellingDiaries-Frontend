from django.contrib import admin
from .models import Diary
# Register your models here.


class DiaryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'user',
    ]
    list_filter = ['user']
    search_fields = ['name']


admin.site.register(Diary, DiaryAdmin)
