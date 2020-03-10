from django.contrib import admin
from .models import Post, PostImage
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['message', 'user']
    list_filter = ['user']
    search_fields = ['message']


admin.site.register(Post, PostAdmin)
admin.site.register(PostImage)
