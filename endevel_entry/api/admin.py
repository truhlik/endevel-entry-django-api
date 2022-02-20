from django.contrib import admin
from .models import *
from django.utils.translation import gettext as _

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title_en", "title_cz", "short_content_en",
                    "short_content_cz", "created_at", "modified_at")
    readonly_fields = ("created_at", "modified_at")
    verbose_name = _("Article")
    verbose_name_plural = _("Articles")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "modified_at")
    readonly_fields = ("created_at", "modified_at")
    verbose_name = _("Tag")
    verbose_name_plural = _("Tags")
