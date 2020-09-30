from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image
from where_to_go import settings


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ['get_images']

    def get_images(self, image_obj):
        if not image_obj.image:
            return 'Картинка ещё не загружена'
        preview = format_html(
            '<img src="{}" style="max-height: 200px; max-width: 200px;"/>',
            image_obj.image.url,
        )
        return preview

    get_images.short_description = 'Screen'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ordering = ['place', 'position']
    raw_id_fields = ['place']
