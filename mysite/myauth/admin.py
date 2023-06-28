from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pk", "fullname"]
    list_display_links = ["pk", "fullname"]