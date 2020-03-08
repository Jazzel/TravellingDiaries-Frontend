from django.contrib import admin
from . import models

# Register your models here.


class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ['group', 'user']
    list_filter = ['group__name', 'user']
    search_fields = ['group__name', 'user']


class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)
admin.site.register(models.GroupMember, GroupMemberAdmin)
