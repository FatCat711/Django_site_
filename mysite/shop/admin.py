from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pk", "title"]
    list_display_links = ["pk", "title"]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["pk", "title"]
    list_display_links = ["pk", "title"]


class ProductInline(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "price"]
    list_display_links = ["pk", "title", "price"]
    inlines = [ProductInline,]


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]
    list_display_links = ["pk", "name"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]
    list_display_links = ["pk", "name"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["pk", "text"]
    list_display_links = ["pk", "text"]
