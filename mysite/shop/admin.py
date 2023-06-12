from django.contrib import admin
from .models import Category, SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pk", "title"]
    list_display_links = ["pk", "title"]


@admin.register(SubCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pk", "title"]
    list_display_links = ["pk", "title"]
