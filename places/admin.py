import traceback

from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image
from where_to_go import settings


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = 'get_images',

    def get_images(self, obj):
        url = ''
        if obj.file_name:
            url = f'{settings.MEDIA_URL}{obj.file_name}'
        try:
            preview = format_html(
                '<img src="{url}" width="200" max-height="200" />'.format(
                    url=url,
                ))
        except Exception:
            print(traceback.format_exc())
            return '-'
        else:
            return preview

    get_images.short_description = 'Screen'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = 'title',

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ordering = 'place', 'position'
