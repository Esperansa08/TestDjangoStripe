from django.contrib import admin

from payments.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price")
    list_filter = ("name",)
    search_fields = ("name",)
