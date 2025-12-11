from django.contrib import admin
from .models import AboutMe

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('headline', 'email', 'created_at')
    search_fields = ('headline', 'email')
    list_filter = ('created_at',)
