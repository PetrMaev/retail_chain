from django.contrib import admin

from links.models import Link


def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


clear_debt.short_description = "Обнуление задолженности перед поставщиком"


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "email",
        "owner",
        "country",
        "city",
        "street",
        "house_number",
        "product_name",
        "product_model",
        "realize_date",
        "provider",
        "network_level",
        "debt",
        "created_at"
    ]
    list_filter = ("city",)
    search_fields = ("email",)
    actions = [clear_debt]
