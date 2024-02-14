from django.contrib import admin
from .models import Job
# Register your models here.

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title',  'date')
    prepopulated_fields = {"slug": ("title",)}
