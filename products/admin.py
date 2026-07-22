from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "category",
        "brand",
        "price",
        "stock",
        "is_featured",
    )

    list_filter = (
        "category",
        "brand",
        "is_featured",
    )

    search_fields = (
        "name",
        "brand",
    )

    ordering = (
        "name",
    )