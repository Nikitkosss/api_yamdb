from django.contrib import admin
from reviews.models import Сategory


@admin.register(Сategory)
class СategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
