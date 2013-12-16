from ads import models
from django.contrib import admin


class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


class AdAdmin(admin.ModelAdmin):
    list_display = (
                    "title",
                    "company_name",
                    "created_at",
                    "geographic_area",
                    "tag_list",
                    )


admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Ad, AdAdmin)
