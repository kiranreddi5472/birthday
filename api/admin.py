from django.contrib import admin
from django.utils.html import format_html
from .models import Wish, Gallery, Dialogue

@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('name', 'message_summary', 'has_image', 'image_preview', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'message')
    readonly_fields = ('created_at', 'full_image_preview')

    def message_summary(self, obj):
        return obj.message[:60] + "..." if len(obj.message) > 60 else obj.message
    message_summary.short_description = "Message"

    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = "Has Photo"

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 40px; border-radius: 4px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Photo Preview"

    def full_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 300px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />', obj.image.url)
        return "No image uploaded for this wish."
    full_image_preview.short_description = "Uploaded Polaroid"


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_thumbnail', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('title',)
    readonly_fields = ('uploaded_at', 'full_image_preview')

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; border-radius: 4px;" />', obj.image.url)
        return "-"
    image_thumbnail.short_description = "Thumbnail"

    def full_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 400px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />', obj.image.url)
        return "-"
    full_image_preview.short_description = "Memory View"


@admin.register(Dialogue)
class DialogueAdmin(admin.ModelAdmin):
    list_display = ('text_summary', 'added_by', 'created_at')
    list_filter = ('created_at', 'added_by')
    search_fields = ('text', 'added_by')
    readonly_fields = ('created_at',)

    def text_summary(self, obj):
        return obj.text[:80] + "..." if len(obj.text) > 80 else obj.text
    text_summary.short_description = "Quote"
