from django.contrib import admin
from memories.models import Memory, Image
from django.contrib.admin import ModelAdmin, TabularInline


class MemoryImageInline(TabularInline):
    model = Image


@admin.register(Memory)
class MemoryAdmin(ModelAdmin):
    model = Memory
    list_display = [field.name for field in Memory._meta.fields]
    inlines = [MemoryImageInline]


@admin.register(Image)
class MemoryImageAdmin(ModelAdmin):
    model = Image
    list_display = [field.name for field in Image._meta.fields]
