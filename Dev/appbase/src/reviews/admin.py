from django.contrib import admin
from .models import Review
# Register your models here.


class ReviewModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Review


admin.site.register(Review, ReviewModelAdmin)
