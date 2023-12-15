from django.contrib import admin
from .models import EmailTemplate


@admin.register(EmailTemplate)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject', 'body']
