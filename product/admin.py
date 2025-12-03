from django.contrib import admin
from .models import *



class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name', 'created_at')
    search_fields = ('id', 'name',)
    ordering = ('id',)


# class AdminProduct(admin.ModelAdmin):
#     list_display = ('id', 'inn', 'sender_pinfl', 'created_at')
#     search_fields = ('id', 'inn', 'sender_pinfl')
#     ordering = ('id',)


admin.site.register(Category, AdminCategory)

